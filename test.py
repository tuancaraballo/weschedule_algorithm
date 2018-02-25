import random
import copy

class daily_demand():
    def __init__(self,demand_name):
        self.demand_name = demand_name

class demand_daily_resource():
    def __init__(self, demands):
        #demands is a list of objects of class demand.
        self.demands = demands
    def add_people(employee_by_order):
        self.people = employee_by_order
    def add_assignments(assigments):
        self.assignments = assignments

class daily_master_schedule():
    def __init__(self, people_shifts):
        #self.people_shifts will be dictionary
        self.people_shifts = people_shifts
        self.people = list(people_shifts.keys())

    def get_people():
        return self.people_shifts.keys()

    def get_time_for_person(person):
        return self.people_shifts[person]

class assign():
    def __init__(self, demand_time_resource, master_schedule, rules):
        self.demand_time_resource = demand_time_resource

        self.master_schedule = master_schedule
        self.rules = rules
    def add_people(self,people):
        self.people = list(people)
    def solve(self):
        if self.rules == "divide_equally":
            #make copy of assignments
            new_list = self.demand_time_resource.demands

            new_list = random.shuffle(new_list)

            #loop through each one randomly
            idx = 0

            num_people = len(self.master_schedule.people)
            people = list(self.master_schedule.people)
            assignments = dict.fromkeys(people)

            while len(self.demand_time_resource.demands) > 0:
                demand = self.demand_time_resource.demands.pop()
                if assignments[people[idx]] == None:
                    assignments[people[idx]] = [demand]

                else:
                    assignments[people[idx]] = assignments[people[idx]] + [demand]

                idx += 1
                if num_people == idx:
                    idx = 0
            return assignments
