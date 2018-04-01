from unittest import TestCase


class TestSolveDemandResourceSchedule(TestCase):
    def test_solveDemandResourceSchedule(self):
        from rooming_assignments import solveDemandResourceSchedule
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/2/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/3/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/4/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/5/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/2/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/3/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/4/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                       {"date": "3/5/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]}
                                       ]}]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/2/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/3/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/4/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/5/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]}
                                     ]},
                       {"key": "Nelligan",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/2/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/3/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/4/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                                     {"date": "3/5/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Nelligan", 1: "Sally", "priority": 1, "num": 1},
                                                              {"key": "Montecute", 1: "Diego", "priority": 2,
                                                               "num": 1}]}]

        sol  =solveDemandResourceSchedule(demand_info, resource_info, instructions)
        print(sol)
        self.fail()
