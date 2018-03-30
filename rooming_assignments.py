from datetime import datetime


# We need three classes to solve the rooming problem
class Schedule:
    def __init__(self, info, assignments):
        self.assignments = assignments
        self.mappingKeyToSchedule = self.__getMappingKeyToSchedule(info)

    def __getMappingKeyToSchedule(self, info):
        result = {}

        for dic in info:
            try:
                key_schedule = {}

                for day in dic["schedule"]:
                    converted_datetime = []
                    for start, end  in day["time"]:
                        converted_datetime.append((datetime.strptime(start, '%H:%M'),datetime.strptime(end, '%H:%M')))

                    key_schedule[day["date"]] = {self.assignments[0]: converted_datetime}
                result[dic["key"]] = key_schedule

            except KeyError:
                print("We could not find a key in dictionary {}".format(dic))
                raise
        return result

    def getKeySchedule(self, key):

        try:
            return self.mappingKeyToSchedule[key]

        except KeyError:
            print("We did not find key")
            raise
    def get_dates_key(self, key):

        return self.mappingKeyToSchedule[key].keys()

    def get_key_schedule_date(self, key, date):

        return self.mappingKeyToSchedule[key][date]

    def find_overlap_single_day(self, int_avail_schedule, ext_avail_schedule):
        '''

        :param internal_key:
        :param external_key:
        :param date:
        :param external_schedule:
        :return: a list of overlapping segments for the two schedules
        '''
        overlap = []
        int_avail_schedule["available"].sort(reverse=True)
        ext_avail_schedule["available"].sort(reverse=True)

        for int_seg in int_avail_schedule["available"]:
            for ext_seg in ext_avail_schedule["available"]:

                if int_seg[1] > ext_seg[0] and ext_seg[1] > int_seg[0]:
                    overlap.append((max([int_seg[0], ext_seg[0]]), min([int_seg[1], ext_seg[1]])))
        print("overlap is ")
        print(overlap)
        return overlap

    def remove_overlap_label(self):
        pass
    #TODO: finish implemting assign overlap
    def assignOverlap(self, internal_key, external_key, external_schedule):
        '''

        :param internal_key: key for either resource or demand
        :param external_key: key for either reosource or demand for other schedule
        :param external_schedule: Schedule for other object
        :return: Does not return, just changes both Schedules in place.
        '''

        internal_key_schedule = self.getKeySchedule(internal_key)
        external_key_schedule = external_schedule.getKeySchedule(external_key)

        #find overlap between two scheduels of two keys
        overlap = {}
        for date in internal_key_schedule.keys():
            if date in external_key_schedule.keys():
                overlap[date] = self.find_overlap_single_day(self.get_key_schedule_date(internal_key, date),
                                                             external_schedule.get_key_schedule_date(external_key, date))

        #then reveal the overlapping schedules
        for date in internal_key_schedule.keys():
            if date in external_key_schedule.keys():
                pass
                #self.remove_overlap_label(date, overlap, external_key)
                #external_schedule.remove_overlap_label(date, overlap, internal_key)

class Rules:

    def __init__(self, rules):
        self.rules = rules
        self.mapping_rule = self.__get_mapping_rule(rules)

    def __get_mapping_rule(self, rules):
        for rule in rules:
            if rule["key"] == "mapping":
                return MappingRule(rule["map"])


class MappingRule:

    def __init__(self, mapping):
        self.demand_to_resources = self.__get_demand_to_resources(mapping)
        self.demand_by_priority = self.__get_demand_by_priority(mapping)

    def get_demand_by_priorities(self):
        return self.demand_by_priority

    def get_resources_for_demand_by_priority(self, demand):
        return self.demand_to_resources[demand]

    @staticmethod
    def __get_demand_to_resources(mapping):
        """
        converts the mapping dictionary to a dictionary that maps demand => list of resouces organized in descending order. 
        :param mapping:  a list of dictionaries with field key, and priority
        :return:  Dictionary that maps demand to resources by order of priority
        """
        demand_to_resources = {}


        for demand_dic in mapping:
            list_resources = []

            for resource_priority in range(1, demand_dic["num"] + 1):
                list_resources.append(demand_dic[int(resource_priority)])

            demand_to_resources[demand_dic["key"]] = list_resources
        return demand_to_resources

    @staticmethod
    def __get_demand_by_priority(mapping):
        '''
        Method to get a list of demand in order by priority to be able to iterate
        :param mapping: a list of dictionaries with field key, and priority
        :return: a list of demand_keys in descending priority.
        '''
        tuples_priority_demand = []

        for demand in mapping:
            tuples_priority_demand.append((demand["priority"], demand["key"]))

        tuples_priority_demand.sort()
        demand_by_priority = []

        for priority, demand in tuples_priority_demand:

            demand_by_priority.append(demand)

        return demand_by_priority

class Solver:
    def __init__(self):
        self.resourceSchedule = None
        self.demandSchedule = None
        self.rules = None

    def addResourceSchedule(self, schedule):
        try:
            self.resourceSchedule = schedule
        except ValueError:
            raise

    def addDemandSchedule(self, schedule):
        try:
            self.demandSchedule = schedule
        except ValueError:
            raise

    def addRules(self, rules):
        self.rules = rules

    def solve(self):
        # check that everything has been added
        if self.resourceSchedule is None or self.demandSchedule is None or self.rules is None:
            raise ValueError("Either the Schedule or the Rules have not been set")

        # apply rules
        self.__applyRules()

        # what optimizatinations are going to be applied
        # self.optimze()
        self.__prepSolution()
        # apply optimizations
        # return self.solution
        # package

    def returnSolution(self):
        return self.solution

    def __prepSolution(self):
        self.solution = {}

        for demand, scheduleDic in self.demandSchedule.mappingKeyToSchedule.items():
            demand_dic = {demand: {}}
            for date, assignment_dic in scheduleDic.items():
                assignments = {}
                for assignment, daySchedule in assignment_dic.items():
                    if assignment != "available":
                        if assignment not in assignments.keys():

                            assignments[assignment] = daySchedule
                        else:
                            assignments[assignment] = assignments[assignment] + daySchedule
                demand_dic[demand][date] = assignments
            self.solution = {**self.solution, **demand_dic}

    def __applyRules(self):

        for rule in self.rules.rules:
            func = self.__switchRules(rule["key"])
            func(rule)

    def __switchRules(self, key):
        switcher = {
            "mapping": self.__applyMapping
        }
        return switcher[key]

    def __applyMapping(self, rule):

        for demand in self.rules.mapping_rule.get_demand_by_priorities():
            for resource in self.rules.mapping_rule.get_resources_for_demand_by_priority(demand):
                #call method in Schedule object that takes a scehdule
                self.demandSchedule.assignOverlap(demand, resource, self.resourceSchedule)

    def __assignOverlapNew(self, demand_key, resource_key):

        for date in self.demandSchedule.getKeySchedule(demand_key).keys():

            if date in self.resourceSchedule.getKeySchedule(resource_key):
                pass
                #self.demandSchedule.assignOverlap(demand_key,resource_key, date)


    def __assignOverlap(self, demandKey, resourceKey):

        for date in self.demandSchedule.getKeySchedule(demandKey).keys():

            if date in self.resourceSchedule.getKeySchedule(resourceKey):



                for demand_segment in self.demandSchedule.getKeySchedule(demandKey)[date]['available']:

                    for resource_segment in self.resourceSchedule.getKeySchedule(resourceKey)[date]['available']:

                        if datetime.strptime(demand_segment[1], '%H:%M') > datetime.strptime(resource_segment[0],
                                                                                             '%H:%M') \
                                and datetime.strptime(demand_segment[0], '%H:%M') < datetime.strptime(
                                    resource_segment[1], '%H:%M'):

                            # print("Found overlapping segments {} " + str(resource_segment))
                            # remove segment
                            start_overlap = demand_segment[0] if datetime.strptime(demand_segment[0], '%H:%M') \
                                                                 > datetime.strptime(resource_segment[0], '%H:%M') else \
                            resource_segment[0]

                            end_overlap = demand_segment[1] if datetime.strptime(demand_segment[1], '%H:%M') \
                                                               < datetime.strptime(resource_segment[1], '%H:%M') else \
                            demand_segment[1]

                            # print("start overlap is {} and end is {}".format(start_overlap, end_overlap))
                            # self.resourceSchedule.getKeySchedule(resourceKey)[date]['available'].remove(resource_segment)
                            if demandKey in self.resourceSchedule.getKeySchedule(resourceKey)[date].keys():
                                self.resourceSchedule.getKeySchedule(resourceKey)[date][demandKey] = \
                                self.resourceSchedule.getKeySchedule(resourceKey)[date][demandKey] \
                                + [(start_overlap, end_overlap)]
                            else:
                                self.resourceSchedule.getKeySchedule(resourceKey)[date][demandKey] = [
                                    (start_overlap, end_overlap)]

                            if resourceKey in self.demandSchedule.getKeySchedule(demandKey)[date].keys():
                                self.demandSchedule.getKeySchedule(demandKey)[date][resourceKey] = \
                                self.demandSchedule.getKeySchedule(demandKey)[date][resourceKey] \
                                + [(start_overlap, end_overlap)]
                            else:
                                self.demandSchedule.getKeySchedule(demandKey)[date][resourceKey] = [
                                    (start_overlap, end_overlap)]
                                # self.demandSchedule.getKeySchedule(demandKey)[date]['need'].remove(demand_segment)

                                # self.demandSchedule.getKeySchedule(demandKey)[date] = {resourceKey: [('8:00', '12:00'), ('13:00', '18:00')]}
                                # self.resourceSchedule.getKeySchedule(resourceKey)[date] = {demandKey: [('8:00', '12:00'), ('13:00', '18:00')]}


def solveDemandResourceSchedule(demand_info, resource_info, given_rules):

    #TODO: create a initializer that creates solver by passing in demand, resource and rules

    demand = Schedule(demand_info, ["available"])
    resource = Schedule(resource_info, ["available"])
    rule_obj = Rules(given_rules)
    print(type(rule_obj))
    solver = Solver()
    solver.addDemandSchedule(demand)
    solver.addResourceSchedule(resource)
    solver.addRules(rule_obj)

    solver.solve()
    return solver.returnSolution()


