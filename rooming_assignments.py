import datetime


# We need three classes to solve the rooming problem
class Schedule():
    def __init__(self, info, assignments):
        self.assignments = assignments
        self.mappingKeyToSchedule = self.__getMappingKeyToSchedule(info)

    def __getMappingKeyToSchedule(self, info):
        result = {}

        for dic in info:
            try:
                key_schedule = {}

                for day in dic["schedule"]:
                    key_schedule[day["date"]] = {self.assignments[0]: day["time"]}
                result[dic["key"]] = key_schedule

            except KeyError:
                print("We could not find a key in dictionary {}".format(dic))
                raise
        return result

    def getKeySchedule(self, key):

        try:
            return self.mappingKeyToSchedule[key]

        except KeyError:
            print("we schould not find key")
            raise


class Rules:
''' Class that will store the rules such as MappingRule and ConstraintRule
'''
    def __init__(self, rules):
        self.rules = rules

class MappingRule:

    def __init__(self, mapping):

        self.DemandToResources = self.__get_demand_to_resources(mapping)


    def get_demand_by_priorities:
        pass

    def get_resources_for_demand_by_priority(self, demand):
        pass

    def __get_demand_to_resources(self, mapping):
        pass


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
        if (self.resourceSchedule is None or self.demandSchedule is None or self.rules is None):
            raise ValueError("Either the Schedule or the Rules have not been set")

        # apply rules
        self.__applyRules()

        # what optimizatinations are going to be applied
        # self.optimze()
        self.__prepSolution()
        # apply optimizations
        # return self.solution
        # package

    def returnSolutino(self):
        return self.solution

    def __prepSolution(self):
        self.solution = {}

        for demand, scheduleDic in self.demandSchedule.mappingKeyToSchedule.items():
            print(demand)
            demand_dic = {demand: {}}
            for date, assignment_dic in scheduleDic.items():
                print("\t" + date)
                assignments = {}
                for assignment, daySchedule in assignment_dic.items():
                    print("\t\t" + assignment)
                    if assignment != "need":
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
        mapping = rule["map"]


        priorities = {}

        #get order of mapping, in what order of demands should we apply the mapping?

        for dic in mapping:

            placeholder = {}
            placeholder["key"] = dic["key"]
            placeholder["num"] = dic["num"]
            for idx in range(1, dic["num"] + 1):
                placeholder[idx] = dic[idx]

            priorities[dic["priority"]] = placeholder

        descending_priorities = list(priorities.keys())
        descending_priorities.sort()

        for priority in descending_priorities:
            key = priorities[priority]

            for idx in range(1, priorities[priority]["num"] + 1):

                self.__assignOverlap(key["key"], key[idx])

    def __assignOverlap(self, demandKey, resourceKey):
=
        for date in self.demandSchedule.getKeySchedule(demandKey).keys():

            if date in self.resourceSchedule.getKeySchedule(resourceKey):
                for demand_segment in self.demandSchedule.getKeySchedule(demandKey)[date]['need']:

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

    demand = Schedule(demand_info, ["need"])
    resource = Schedule(resource_info, ["available"])
    rule_obj = Rules(given_rules)

    solver = Solver()
    solver.addDemandSchedule(demand)
    solver.addResourceSchedule(resource)
    solver.addRules(rule_obj)

    solver.solve()
    return solver.returnSolution
