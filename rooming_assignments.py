from datetime import datetime
from collections import namedtuple

def solve_demand_resource_schedule(demand_schedule, resource_schedule, instructions):
    # set up solver and
    # Ωadd information
    solver = Solver()
    solver.set_demand_schedule(demand_schedule)
    solver.set_resource_schedule(resource_schedule)
    solver.set_instructions(instructions)

    solver.solve()
    return solver.return_solution()

##########################################
class Solver:
    def __init__(self):
        self.resource_schedule = None
        self.demand_schedule   = None
        self.instructions      = None
        self.solution = None

    def set_resource_schedule(self, schedule):
        self.resource_schedule = Schedule(schedule)

    def set_demand_schedule(self, schedule):
        self.demand_schedule = Schedule(schedule)

    def set_instructions(self, instructions):
        self.instructions = Instructions(instructions)

    def apply_instruction(self, instruction):

        algorithm = self.find_algorithm(instruction)
        algorithm()

    def find_algorithm(self, instruction):
        switcher = {
            "mapping": self._call_mapping_algorithm

        }
        return switcher[instruction["key"]]

    def solve(self):
        for instruction in self.instructions.get_instructions_by_order():
            self.apply_instruction(instruction)

        self._prep_solution()

    def return_solution(self):
        return self.solution

    def _prep_solution(self):
        self.solution = {}
        self.solution["demand"] = self.demand_schedule.format_solution()
        self.solution["resource"] = self.resource_schedule.format_solution()

    def _switch_rules(self, key):
        switcher = {
            "mapping": self._call_mapping_algorithm
        }
        return switcher[key]

    def _call_mapping_algorithm(self):
        # call mapping algorithm on Demand Schedule with resource and mapping
        self.demand_schedule.run_mapping_with(self.resource_schedule,
                                              self.instructions.get_mapping())

class Schedule:
    def __init__(self, schedule_info):
        self.assignments = ["available"]
        self.schedule = self._get_schedules_for_keys(schedule_info)
        self.reformatted_solution_to_return = None

    def format_solution(self):
        if self.reformatted_solution_to_return is None:
            self.reformatted_solution_to_return = self._transform_solution()

        return self.reformatted_solution_to_return
    def _transform_solution(self):
        reformatted_solution = {}
        for key, schedule in self.schedule.items():
            reformatted_solution[key] = schedule
        return reformatted_solution

    def _get_schedules_for_keys(self, all_key_schedules):
        # TODO: Breakdown this method

        def convert_to_datetime_obj(time_interval):
            return datetime.strptime(time_interval[0], '%H:%M'), datetime.strptime(time_interval[1], '%H:%M')

        reformatted_schedule = {}
        for individual_key_schedule in all_key_schedules:

            reformatted_key_schedule = {}

            for day_key_schedule in individual_key_schedule["schedule"]:
                converted_datetime = []
                for time_interval in day_key_schedule["time"]:
                    converted_datetime.append(convert_to_datetime_obj(time_interval))

                reformatted_key_schedule[day_key_schedule["date"]] = {self.assignments[0]: sorted(converted_datetime)}
            reformatted_schedule[individual_key_schedule["key"]] = reformatted_key_schedule

        return reformatted_schedule

    def get_key_dates(self, key):
        return self.schedule[key].keys()

    def get_dates_key(self, key):
        return self.schedule[key].keys()

    def get_key_schedule_date(self, key, date):
        return self.schedule[key][date]

    def run_mapping_with(self, resource_schedule, mapping_obj):
        '''
        The mapping algorithm works by:
        For each demand-resource pair:
            for each date that both demand-resource pair are available:
                Find overlapping segments and assign to each other
        :param resource_schedule: scehdule of the availability of the resource
        :param mapping_obj: of Class Mapping
        :return:
        '''

        # for every demand we have a mapping for
        for demand in mapping_obj.get_demands_ordered_by_priority():
            # for resources that a demand has a possible match with
            for resource in mapping_obj.get_resources_for_demand_ordered_by_priority(demand):
                self.apply_a_single_mapping_between(demand,
                                                    resource,
                                                    resource_schedule)

    def find_overlap_single_day(self, schedule_pair, key_pair):
        '''

        :param internal_key:
        :param external_key:
        :param date:
        :param external_schedule:
        :return: a list of overlapping segments for the two schedules
        '''

        def either_avail_schedule_empty(demand_avail_schedule, resource_avail_schedule):
            return len(demand_avail_schedule) == 0 or len(resource_avail_schedule) == 0


        demand_key_schedule, resource_key_schedule = schedule_pair
        #ext_key_schedule = schedule_pair.resource_schedule
        demand_key, resource_key = key_pair
        #resource_key = key_pair.resource_key

        demand_avail_schedule = demand_key_schedule["available"]
        resource_avail_schedule = resource_key_schedule["available"]

        if either_avail_schedule_empty(demand_avail_schedule, resource_avail_schedule):
            return

        updated_demand_avail_schedule = []
        updated_resource_avail_schedule = []
        overlap_result = []

        while (len(demand_avail_schedule) > 0 and len(resource_avail_schedule) > 0):
            demand_trailing, resource_trailing, overlap_add = self._find_overlap(demand_avail_schedule, resource_avail_schedule)

            updated_demand_avail_schedule   += demand_trailing
            updated_resource_avail_schedule += resource_trailing
            overlap_result += overlap_add

            if len(demand_avail_schedule) == 0 and len(resource_avail_schedule) != 0:
                updated_resource_avail_schedule += resource_avail_schedule

            if len(resource_avail_schedule) == 0 and len(demand_avail_schedule) != 0:

                updated_demand_avail_schedule += demand_avail_schedule

        # update schedules
        demand_key_schedule["available"] = updated_demand_avail_schedule
        resource_key_schedule["available"] = updated_resource_avail_schedule
        resource_key_schedule[demand_key] = overlap_result
        demand_key_schedule[resource_key] = overlap_result

    def _find_overlap(self, demand_avail_schedule, resource_avail_schedule):

        def segments_non_overlapping(segment1, segment2):
            return segment1[1] <= segment2[0] or segment2[1] <= segment1[0]

        def segment1_ahead_segment2(segment1, segment2):
            return segment2[1] <= segment1[0]

        def segment2_ahead_segment1(segment1, segment2):
            return segment1[1] <= segment2[0]

        def remove_earlier_segment(segment1, segment2, t1, t2):
            if segment1_ahead_segment2(segment1, segment2):
                # no overlap,so remover trailing from list1 and add to to available
                t2.pop(0)
                return [], [segment2], []
            if segment2_ahead_segment1(segment1, segment2):
                # no overlap and segment2 is trailing
                t1.pop(0)
                return [segment1], [], []

        def overlap_of_segments(segment1, segment2):
            return (max(segment1[0], segment2[0]), min(segment1[1], segment2[1]))
        # TODO:break down this method

        segment1 = demand_avail_schedule[0]
        segment2 = resource_avail_schedule[0]
        if segments_non_overlapping(segment1, segment2):
            return remove_earlier_segment(segment1, segment2, demand_avail_schedule, resource_avail_schedule)

        overlap = overlap_of_segments(segment1, segment2)


        # now we have to figure out how to update available time, both for
        # case 1: they are exactly same segment
        if segment1[0] == overlap[0] and segment1[1] == overlap[1] and segment2[0] == overlap[0] and \
                        segment2[1] == overlap[1]:

            demand_avail_schedule.pop(0)
            resource_avail_schedule.pop(0)

            return [], [], [overlap]

        # case2: they start same time, but 1 is ends later than other
        if segment1[0] == overlap[0] and segment2[0] == overlap[0] and (segment1[1] != overlap[1] or segment2[1] != \
                overlap[1]):

            if segment1[1] > segment2[1]:

                resource_avail_schedule.pop(0)
                demand_avail_schedule.pop(0)

                demand_avail_schedule.insert(0, (overlap[1], segment1[1]))

                return [], [], [overlap]
            else:
                resource_avail_schedule.pop(0)
                demand_avail_schedule.pop(0)

                resource_avail_schedule.insert(0, (overlap[1], segment2[1]))

                return [], [], [overlap]

        # case3: they end same time, but 1 is starts sooner than other
        if segment1[1] == overlap[1] and segment2[1] == overlap[1] and (segment1[0] != overlap[0] or segment2[0] != \
                overlap[1]):

            if segment1[0] < segment2[0]:

                demand_avail_schedule.pop(0)
                resource_avail_schedule.pop(0)

                return [(segment1[0], overlap[0])], [], [overlap]

            else:
                demand_avail_schedule.pop(0)
                resource_avail_schedule.pop(0)

                return [], [(segment2[0], overlap[0])], [overlap]
        # case4: one is starts sooner and ends later, completely overlapping one

        if segment1[0] > segment2[0] and segment1[1] < segment2[1]:

            demand_avail_schedule.pop(0)
            resource_avail_schedule.pop(0)

            resource_avail_schedule.insert(0, (overlap[1], segment2[1]))

            return [], [(segment2[0], overlap[0])], [overlap]

        if segment2[0] > segment1[0] and segment2[1] < segment1[1]:
            demand_avail_schedule.pop(0)
            resource_avail_schedule.pop(0)

            demand_avail_schedule.insert(0, (overlap[1], segment1[1]))

            return [(segment1[0], overlap[0])], [], [overlap]

        # case 5: segments do not either start together or end together, but overlap. like a random middle segemnt

        if segment1[1] > segment2[1]:
            demand_avail_schedule.pop(0)
            resource_avail_schedule.pop(0)

            demand_avail_schedule.insert(0, (overlap[1], segment1[1]))

            return [], [(segment2[0], overlap[0])], [overlap]

        if segment2[1] > segment1[1]:
            demand_avail_schedule.pop(0)
            resource_avail_schedule.pop(0)

            resource_avail_schedule.insert(0, (overlap[1], segment2[1]))

            return [(segment1[0], overlap[0])], [], [overlap]

        assert ("Should have not gotten here")

    @staticmethod
    def segments_overlap(int_seg, ext_seg):
        return int_seg[1] > ext_seg[0] and ext_seg[1] > int_seg[0]

    def apply_a_single_mapping_between(self, demand_key, resource_key, external_schedule):
        '''
        For a combination of demand and resource, this method will assign any overlap to each other
        :param demand_key: id for demand, given that this method will be called in the context of
                            schedule that has demand, demand_key_schedule will be called with self.
        :param resource_key: id for resource
        :param external_schedule: Schedule for other object
        :return: Does not return, just changes both Schedules in place.
        '''
        Schedule_Pair = namedtuple("Schedule_Pair","demand_schedule resource_schedule")
        Key_Pair = namedtuple("Key_Pair", "demand_key resource_key")

        demand_key_schedule = self.get_key_dates(demand_key)
        resource_key_schedule = external_schedule.get_key_dates(resource_key)


        # find overlap between two scheduels of two keys, overlap
        for date in demand_key_schedule:
            if date in resource_key_schedule:
                # readability reasons, pair them up.
                schedules = Schedule_Pair(self.get_key_schedule_date(demand_key, date),
                                 external_schedule.get_key_schedule_date(resource_key, date))
                keys = Key_Pair(demand_key, resource_key)

                self.find_overlap_single_day(schedules, keys)


##########################################
class Instructions:
    def __init__(self, instructions):
        self.instructions_by_order = self._order_instructions(instructions)
        self.number_of_instructions = len(instructions)
        self.mapping = self.__create_mapping(instructions)

    def __create_mapping(self, rules):
        for rule in rules:
            if rule["key"] == "mapping":
                return Mapping(rule["map"])

    def _order_instructions(self, instructions):
        instructions_by_order = [None] * len(instructions)

        for num_order in range(0, len(instructions)):
            index_order = instructions[num_order]["order"] - 1
            instructions_by_order[index_order] = instructions[num_order]

        return instructions_by_order

    def get_mapping(self):
        return self.mapping

    def get_instructions_by_order(self):
        return self.instructions_by_order

##########################################
class Mapping:
    def __init__(self, mapping):
        # need to reformat mapping of demands to resources to enable getters
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

        # make a list of tuples [(priority, demand_key)] and order them
        demands_ordered_by_priority = find_demands_and_priority(mapping)
        # remove priority so that is only a list of demands [demand1,demand2] ordered by descending priority
        demands_ordered_by_priority = remove_priority(demands_ordered_by_priority)

        return demands_ordered_by_priority

##########################################

