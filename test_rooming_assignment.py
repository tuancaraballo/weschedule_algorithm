from unittest import TestCase


class TestSolveDemandResourceSchedule(TestCase):
    def test_solveDemandResourceSchedule(self):
        #end to end testing

        from rooming_assignments import solve_demand_resource_schedule
        import datetime
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
        correc_sol = {'resource':
                          {'Sally': {'3/2/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/1/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/3/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/5/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/4/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}},
                           'Diego': {'3/2/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/3/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/5/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}, '3/4/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))], 'available': []}}},
                      'demand':
                          {'Montecute': {'3/2/2018': {'available': [], 'Diego': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/1/2018': {'available': [], 'Diego': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/3/2018': {'available': [], 'Diego': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/5/2018': {'available': [], 'Diego': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/4/2018': {'available': [], 'Diego': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}},
                           'Nelligan': {'3/2/2018': {'available': [], 'Sally': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/1/2018': {'available': [], 'Sally': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/3/2018': {'available': [], 'Sally': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/5/2018': {'available': [], 'Sally': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}, '3/4/2018': {'available': [], 'Sally': [(datetime.datetime(1900, 1, 1, 13, 0), datetime.datetime(1900, 1, 1, 18, 0)), (datetime.datetime(1900, 1, 1, 8, 0), datetime.datetime(1900, 1, 1, 12, 0))]}}}}
        sol  = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        assert sol == correc_sol

    def test_2(self):
        pass
