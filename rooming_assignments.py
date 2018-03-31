from datetime import datetime


# We need three classes to solve the rooming problem
class Schedule:
    def __init__(self, schedule_info):
        self.assignments = ["available"]
        self.schedule = self._get_schedules_for_keys(schedule_info)

    def _get_schedules_for_keys(self, all_key_schedules):
        reformatted_schedule = {}

        for individual_key_schedule in all_key_schedules:


            reformatted_key_schedule = {}

            for day_key_schedule in individual_key_schedule["schedule"]:
                converted_datetime = []
                for time_interval  in day_key_schedule["time"]:
                    converted_datetime.append(self.convert_to_datetime_obj(time_interval))
                reformatted_key_schedule[day_key_schedule["date"]] = {self.assignments[0]: converted_datetime}
            reformatted_schedule [individual_key_schedule["key"]] = reformatted_key_schedule

        return reformatted_schedule

    def convert_to_datetime_obj(self, time_interval):
        return datetime.strptime(time_interval[0], '%H:%M'),datetime.strptime(time_interval[1], '%H:%M')

    def get_key_schedule(self, key):
        return self.schedule[key]

    def get_dates_key(self, key):
        return self.schedule[key].keys()

    def get_key_schedule_date(self, key, date):
        return self.schedule[key][date]

    def find_overlap_single_day(self, int_avail_schedule, ext_avail_schedule, internal_key, external_key):
        '''

        :param internal_key:
        :param external_key:
        :param date:
        :param external_schedule:
        :return: a list of overlapping segments for the two schedules
        '''

        def replace_segment(old_seg, overlap_seg):
            if old_seg[0] == overlap_seg[0] and old_seg[1] == overlap_seg[1]:
                return None

        overlap = []
        int_avail_schedule["available"].sort(reverse=True)
        ext_avail_schedule["available"].sort(reverse=True)

        t1 = int_avail_schedule["available"]
        t2 = ext_avail_schedule["available"]

        new_int_avail = []
        new_ext_avail = []

        t1_result = []
        t2_result = []
        overlap_result = []

        while (len(t1) > 0 and len(t2) > 0):

            t1_trailing, t2_trailing, overlap_add = self._find_overlap(t1, t2)

            t1_result += t1_trailing
            t2_result += t2_trailing
            overlap_result += overlap_add

            if len(t1) == 0 and len(t2) != 0:
                t2_result += t2

            if len(t2) == 0 and len(t1) != 0:
                t1_result += t1
        int_avail_schedule["available"] = t1
        ext_avail_schedule["available"] = t2
        ext_avail_schedule[internal_key] = overlap_result
        int_avail_schedule[external_key] = overlap_result


    def _find_overlap(self,t1, t2):
        segment1 = t1[0]
        segment2 = t2[0]

        if segment1[1] < segment2[0]:
            # no overlap,so remover trailing from list1 and add to to available
            t1.pop(0)
            return [segment1], [], []
        if segment2[1] < segment1[0]:
            # no overlap and segment2 is trailing
            t2.pop(0)
            return [], [segment2], []

        overlap = (max(segment1[0], segment2[0]), min(segment1[1], segment2[1]))

        # now we have to figure out how to update available time, both for
        # case 1: they are exactly same segment
        if segment1[0] == overlap[0] and segment1[1] == overlap[1] and segment1[0] == overlap[0] and segment2[1] == \
                overlap[1]:
            t1.pop(0)
            t2.pop(0)

            return [], [], [overlap]

        # case2: they start same time, but 1 is ends later  than other

        if segment1[0] == overlap[0] and segment2[0] == overlap[0] and segment1[1] != overlap[1] or segment2[1] != \
                overlap[1]:

            if segment1[1] > segment2[1]:

                t2.pop(0)
                t1.pop(0)

                t1.insert(0, (overlap[1], segment1[1]))

                return [], [], [overlap]
            else:
                t2.pop(0)
                t1.pop(0)

                t2.insert(0, (overlap[1], segment2[1]))

                return [], [], [overlap]

        # case3: they end same time, but 1 is starts sooner than other
        if segment1[1] == overlap[1] and segment2[1] == overlap[1] and segment1[0] != overlap[0] or segment2[0] != \
                overlap[1]:

            if segment1[0] < segment2[0]:

                t1.pop(0)
                t2.pop(0)

                return [(segment1[0], overlap[0])], [], [overlap]

            else:
                t1.pop(0)
                t2.pop(0)

                return [], [(segment2[0], overlap[0])], [overlap]
        # case4: one is starts sooner and ends later, completely overlapping one

        if segment1[0] > segment2[0] and segment1[1] < segment2[1]:
            t1.pop()
            t2.pop()

            t2.insert(0, (overlap[1], segment2[1]))

            return [], [(segment2[0], overlap[0])], [overlap]

        if segment2[0] > segment1[0] and segment2[1] < segment1[1]:
            t1.pop()
            t2.pop()

            t1.insert(0, (overlap[1], segment1[1]))

            return [(segment1[0], overlap[0])], [], [overlap]

        # case 5: segments do not either start together or end together, but overlap. like a random middle segemnt

        if segment1[1] > segment2[1]:
            t1.pop()
            t2.pop()

            t1.insert(0, (overlap[1], segment1[1]))

            return [], [(segment2[0], overlap[0])], [overlap]

        if segment2[1] > segment1[1]:
            t1.pop()
            t2.pop()

            t2.insert(0, (overlap[1], segment2[1]))

            return [(segment1[0], overlap[0])], [], [overlap]

        assert ("Should have not gotten here")

        for int_seg in int_avail_schedule["available"]:
            for ext_seg in ext_avail_schedule["available"]:
                if self.segments_overlap(int_seg, ext_seg):

                    single_overlap = start_end_overlap(int_seg, ext_seg)
                    x = replace_segment(int_seg, single_overlap)
                    print(x)

                    new_int_avail.append(replace_segment(int_seg, single_overlap))
                    new_ext_avail.append(replace_segment(ext_seg, single_overlap))
                    overlap.append(single_overlap)

                else:
                    new_int_avail.append(int_seg)
                    new_ext_avail.append(ext_seg)

        int_avail_schedule["available"] = [time_seg for time_seg in new_int_avail if time_seg is not None]
        int_avail_schedule[external_key] = overlap
        ext_avail_schedule["available"] = [time_seg for time_seg in new_ext_avail if time_seg is not None]
        ext_avail_schedule[internal_key] = overlap


        print("new internal schedule ")
        print(self.schedule)
        return overlap
    def segments_overlap(self, int_seg, ext_seg):
        return int_seg[1] > ext_seg[0] and ext_seg[1] > int_seg[0]

    def remove_overlap_single_day_and_label(self, overlap_segments, date, overlap_label, internal_key):
        # Get the schedule from the date
            # For the segment that there is overlap, divide segment into non-overlap and overlap segment
            # available = non-overlap
            # label = overlap

        date_key_schedule_avail = self.get_key_schedule_date(internal_key, date)["available"]

        for avail_segment in date_key_schedule_avail:
            for single_overlap_segment in overlap_segments:
                if self.segments_overlap(avail_segment, single_overlap_segment):
                    self.get_key_schedule_date(internal_key, date)[overlap_label] = single_overlap_segment

    #TODO: finish implemting assign overlap
    def assignOverlap(self, internal_key, external_key, external_schedule):
        '''

        :param internal_key: key for either resource or demand
        :param external_key: key for either reosource or demand for other schedule
        :param external_schedule: Schedule for other object
        :return: Does not return, just changes both Schedules in place.
        '''

        internal_key_schedule = self.get_key_schedule(internal_key)
        external_key_schedule = external_schedule.get_key_schedule(external_key)

        #find overlap between two scheduels of two keys
        overlap = {}
        for date in internal_key_schedule.keys():
            if date in external_key_schedule.keys():
                overlap[date] = self.find_overlap_single_day(self.get_key_schedule_date(internal_key, date),
                                                             external_schedule.get_key_schedule_date(external_key, date), internal_key, external_key)


        #then reveal the overlapping schedules
        for date in internal_key_schedule.keys():
            if date in external_key_schedule.keys():

                self.remove_overlap_single_day_and_label(overlap[date],date, external_key, internal_key)
                external_schedule.remove_overlap_single_day_and_label(overlap[date], date, internal_key, external_key)

class Instructions:

    def __init__(self, instructions):
        self.instructions_by_order = self._order_instructions(instructions)
        self.number_of_instructions = len(instructions)
        self.mapping_rule = self.__get_mapping_rule(instructions)

    def __get_mapping_rule(self, rules):
        for rule in rules:
            if rule["key"] == "mapping":
                return MappingRule(rule["map"])

    def _order_instructions(self, instructions):
        instructions_by_order = [None] * len(instructions)
        print(instructions)
        for num_order in range(0, len(instructions)):
            index_order = instructions[num_order]["order"] - 1
            instructions_by_order[index_order] = instructions[num_order]

        return instructions_by_order

    def get_instructions_by_order(self):
        print("we sent these ")
        print(self.instructions_by_order)
        print()
        return self.instructions_by_order


class MappingRule:

    def __init__(self, mapping):
        #need to reformat mapping of demands to resources to enable getters
        self.demand_to_resources_by_resource_priority = self._set_demand_to_resources_by_resource_priority(mapping)
        self.demands_ordered_by_priority = self._set_demand__ordered_by_priority(mapping)

    def get_demands_ordered_by_priority(self):
        return self.demands_ordered_by_priority

    def get_resources_for_demand_ordered_by_priority(self, demand):
        return self.demand_to_resources_by_resource_priority[demand]

    @staticmethod
    def _set_demand_to_resources_by_resource_priority(mapping):
        """
        converts the mapping dictionary to a dictionary that maps demand => list of resouces organized in descending order. 
        :param mapping:  a list of dictionaries with field key, and priority
        :return:  Dictionary that maps demand to resources by order of priority
        """
        demand_to_resources_by_resource_priority = {}

        for individual_demand_mapping in mapping:
            resources_ordered_by_priority = []

            for resource_priority in range(1, individual_demand_mapping["num"] + 1):
                resources_ordered_by_priority.append(individual_demand_mapping[int(resource_priority)])

            demand_to_resources_by_resource_priority[individual_demand_mapping["key"]] = resources_ordered_by_priority
        return demand_to_resources_by_resource_priority

    @staticmethod
    def _set_demand__ordered_by_priority(mapping):
        '''
        Method to get a list of demands in order by priority to be able to iterate
        :param mapping: a list of dictionaries with field key, and priority
        :return: a list of demand_keys in descending priority.['Dr. Nelligan', 'Dr. Montecute']
        '''
        def find_demands_and_priority(mapping):
            demands = []
            for individual_demand in mapping:
                demands.append((individual_demand["priority"], individual_demand["key"]))
            demands.sort()
            return demands

        def remove_priority(demands_ordered_by_priority):
            demands = []

            for priority, demand in demands_ordered_by_priority:
                demands.append(demand)
            return demands

        #make a list of tuples [(priority, demand_key)] and order them
        demands_ordered_by_priority = find_demands_and_priority(mapping)
        #remove priority so that is only a list of demands [demand1,demand2] ordered by descending priority
        demands_ordered_by_priority = remove_priority(demands_ordered_by_priority)

        return demands_ordered_by_priority

class Solver:
    def __init__(self):
        self.resource_schedule = None
        self.demandSchedule = None
        self.instructions = None

    def set_resource_schedule(self, schedule):
        self.resource_schedule = Schedule(schedule)


    def set_demand_schedule(self, schedule):
        self.demandSchedule = Schedule(schedule)

    def set_instructions(self, instructions):
        self.instructions = Instructions(instructions)
    def applyInstruction(self, instruction):

        algorithm = self.find_algorithm(instruction)
        print(algorithm)
        algorithm()

    def find_algorithm(self, instruction):
        switcher = {
            "mapping": self.__applyMapping

        }

        return switcher[instruction["key"]]

        return
    def solve(self):

        for instruction in self.instructions.get_instructions_by_order():
            print(instruction)
            self.applyInstruction(instruction)


        #self.__applyRules()

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

        for demand, scheduleDic in self.demandSchedule.schedule.items():
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

        for rule in self.instructions.rules:
            func = self.__switchRules(rule["key"])
            func(rule)

    def __switchRules(self, key):
        switcher = {
            "mapping": self.__applyMapping
        }
        return switcher[key]

    def __applyMapping(self):

        for demand in self.instructions.mapping_rule.get_demands_ordered_by_priority():
            for resource in self.instructions.mapping_rule.get_resources_for_demand_ordered_by_priority(demand):
                #call method in Schedule object that takes a scehdule
                self.demandSchedule.assignOverlap(demand, resource, self.resource_schedule)


def solveDemandResourceSchedule(demand_schedule, resource_schedule, instructions):

    #set up solver and add information
    solver = Solver()
    solver.set_demand_schedule(demand_schedule)
    solver.set_resource_schedule(resource_schedule)
    solver.set_instructions(instructions)

    #solve
    solver.solve()
    return solver.returnSolution()


