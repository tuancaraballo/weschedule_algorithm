from unittest import TestCase
import pprint

class TestSolveDemandResourceSchedule(TestCase):
    #end to end testing

    def test_solve_simple_all_overlapping(self):
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
        correc_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/2/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/3/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/4/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/5/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []}},
            'Nelligan': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                 datetime.datetime(1900, 1, 1, 12, 0)),
                                                (datetime.datetime(1900, 1, 1, 13, 0),
                                                 datetime.datetime(1900, 1, 1, 18, 0))],
                                      'available': []},
                         '3/2/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                 datetime.datetime(1900, 1, 1, 12, 0)),
                                                (datetime.datetime(1900, 1, 1, 13, 0),
                                                 datetime.datetime(1900, 1, 1, 18, 0))],
                                      'available': []},
                         '3/3/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                 datetime.datetime(1900, 1, 1, 12, 0)),
                                                (datetime.datetime(1900, 1, 1, 13, 0),
                                                 datetime.datetime(1900, 1, 1, 18, 0))],
                                      'available': []},
                         '3/4/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                 datetime.datetime(1900, 1, 1, 12, 0)),
                                                (datetime.datetime(1900, 1, 1, 13, 0),
                                                 datetime.datetime(1900, 1, 1, 18, 0))],
                                      'available': []},
                         '3/5/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                 datetime.datetime(1900, 1, 1, 12, 0)),
                                                (datetime.datetime(1900, 1, 1, 13, 0),
                                                 datetime.datetime(1900, 1, 1, 18, 0))],
                                      'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/2/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/3/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/4/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/5/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []}},
              'Sally': {'3/1/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                   datetime.datetime(1900, 1, 1, 12, 0)),
                                                  (datetime.datetime(1900, 1, 1, 13, 0),
                                                   datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/2/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                   datetime.datetime(1900, 1, 1, 12, 0)),
                                                  (datetime.datetime(1900, 1, 1, 13, 0),
                                                   datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/3/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                   datetime.datetime(1900, 1, 1, 12, 0)),
                                                  (datetime.datetime(1900, 1, 1, 13, 0),
                                                   datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/4/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                   datetime.datetime(1900, 1, 1, 12, 0)),
                                                  (datetime.datetime(1900, 1, 1, 13, 0),
                                                   datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/5/2018': {'Nelligan': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                   datetime.datetime(1900, 1, 1, 12, 0)),
                                                  (datetime.datetime(1900, 1, 1, 13, 0),
                                                   datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []}}}}
        sol  = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        assert sol == correc_sol

    def test_solver_all_non_overlapping(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime

        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("1:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/2/2018", "time": [("1:00", "6:00"), ("19:00", "22:00")]},
                                       {"date": "3/3/2018", "time": [("4:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/4/2018", "time": [("2:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/5/2018", "time": [("1:00", "7:00"), ("19:00", "22:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("1:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/2/2018", "time": [("2:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/3/2018", "time": [("1:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/4/2018", "time": [("4:00", "5:00"), ("19:00", "22:00")]},
                                       {"date": "3/5/2018", "time": [("1:00", "5:00"), ("19:00", "22:00")]}
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [],
                                       'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 0)),
                                                     (datetime.datetime(1900, 1, 1, 13, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]},
                          '3/2/2018': {'Diego': [],
                                       'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 0)),
                                                     (datetime.datetime(1900, 1, 1, 13, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]},
                          '3/3/2018': {'Diego': [],
                                       'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 0)),
                                                     (datetime.datetime(1900, 1, 1, 13, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]},
                          '3/4/2018': {'Diego': [],
                                       'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 0)),
                                                     (datetime.datetime(1900, 1, 1, 13, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]},
                          '3/5/2018': {'Diego': [],
                                       'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 0)),
                                                     (datetime.datetime(1900, 1, 1, 13, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]}},
            'Nelligan': {'3/1/2018': {'Sally': [],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 12, 0)),
                                                    (datetime.datetime(1900, 1, 1, 13, 0),
                                                     datetime.datetime(1900, 1, 1, 18, 0))]},
                         '3/2/2018': {'Sally': [],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 12, 0)),
                                                    (datetime.datetime(1900, 1, 1, 13, 0),
                                                     datetime.datetime(1900, 1, 1, 18, 0))]},
                         '3/3/2018': {'Sally': [],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 12, 0)),
                                                    (datetime.datetime(1900, 1, 1, 13, 0),
                                                     datetime.datetime(1900, 1, 1, 18, 0))]},
                         '3/4/2018': {'Sally': [],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 12, 0)),
                                                    (datetime.datetime(1900, 1, 1, 13, 0),
                                                     datetime.datetime(1900, 1, 1, 18, 0))]},
                         '3/5/2018': {'Sally': [],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 12, 0)),
                                                    (datetime.datetime(1900, 1, 1, 13, 0),
                                                     datetime.datetime(1900, 1, 1, 18, 0))]}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 1, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/2/2018': {'Montecute': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 2, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/3/2018': {'Montecute': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 1, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/4/2018': {'Montecute': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 4, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/5/2018': {'Montecute': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 1, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]}},
              'Sally': {'3/1/2018': {'Nelligan': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 1, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/2/2018': {'Nelligan': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 1, 0),
                                                    datetime.datetime(1900, 1, 1, 6, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/3/2018': {'Nelligan': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 4, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/4/2018': {'Nelligan': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 2, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]},
                        '3/5/2018': {'Nelligan': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 1, 0),
                                                    datetime.datetime(1900, 1, 1, 7, 0)),
                                                   (datetime.datetime(1900, 1, 1, 19, 0),
                                                    datetime.datetime(1900, 1, 1, 22, 0))]}}}}

        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        assert sol == correct_sol

    def test_solver_multiple_matching_resources(self):
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
                                     ]}]

        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                        1:"Sally", "priority": 1, "num": 2, 2:"Diego"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/2/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/3/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/4/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []},
                          '3/5/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))]},
                        '3/2/2018': {'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))]},
                        '3/3/2018': {'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))]},
                        '3/4/2018': {'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))]},
                        '3/5/2018': {'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))]}},
              'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/2/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/3/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/4/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []},
                        '3/5/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []}}}}
        assert sol == correct_sol
 #

    def test_solver_alternating_pattern(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime

        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "9:00"),("10:00", "11:00"),
                                                                     ("12:00", "13:00"),
                                                                     ("14:00", "15:00"), ("16:00", "17:00")]}
                                       ]}]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "18:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 1}]}]

        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 9, 0)),
                                                 (datetime.datetime(1900, 1, 1, 10, 0),
                                                  datetime.datetime(1900, 1, 1, 11, 0)),
                                                 (datetime.datetime(1900, 1, 1, 12, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0)),
                                                 (datetime.datetime(1900, 1, 1, 14, 0),
                                                  datetime.datetime(1900, 1, 1, 15, 0)),
                                                 (datetime.datetime(1900, 1, 1, 16, 0),
                                                  datetime.datetime(1900, 1, 1, 17, 0))],
                                       'available': [(datetime.datetime(1900, 1, 1, 9, 0),
                                                      datetime.datetime(1900, 1, 1, 10, 0)),
                                                     (datetime.datetime(1900, 1, 1, 11, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 0)),
                                                     (datetime.datetime(1900, 1, 1, 13, 0),
                                                      datetime.datetime(1900, 1, 1, 14, 0)),
                                                     (datetime.datetime(1900, 1, 1, 15, 0),
                                                      datetime.datetime(1900, 1, 1, 16, 0)),
                                                     (datetime.datetime(1900, 1, 1, 17, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]}}},
 'resource': {'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 9, 0)),
                                                   (datetime.datetime(1900, 1, 1, 10, 0),
                                                    datetime.datetime(1900, 1, 1, 11, 0)),
                                                   (datetime.datetime(1900, 1, 1, 12, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0)),
                                                   (datetime.datetime(1900, 1, 1, 14, 0),
                                                    datetime.datetime(1900, 1, 1, 15, 0)),
                                                   (datetime.datetime(1900, 1, 1, 16, 0),
                                                    datetime.datetime(1900, 1, 1, 17, 0))],
                                     'available': []}}}}

        assert sol == correct_sol

    def test_solver_2_alternating_resources(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime

        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "9:00"), ("10:00", "11:00"),
                                                                     ("12:00", "13:00"),
                                                                     ("14:00", "15:00"), ("16:00", "17:00")]},
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("9:00", "10:00"), ("11:00", "12:00"),
                                                                     ("13:00", "14:00"),("15:00", "16:00"),
                                                                     ("17:00", "18:00")]},
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "18:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 2,2:"Diego"}]}]

        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 9, 0),
                                                  datetime.datetime(1900, 1, 1, 10, 0)),
                                                 (datetime.datetime(1900, 1, 1, 11, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 0),
                                                  datetime.datetime(1900, 1, 1, 14, 0)),
                                                 (datetime.datetime(1900, 1, 1, 15, 0),
                                                  datetime.datetime(1900, 1, 1, 16, 0)),
                                                 (datetime.datetime(1900, 1, 1, 17, 0),
                                                  datetime.datetime(1900, 1, 1, 18, 0))],
                                       'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 9, 0)),
                                                 (datetime.datetime(1900, 1, 1, 10, 0),
                                                  datetime.datetime(1900, 1, 1, 11, 0)),
                                                 (datetime.datetime(1900, 1, 1, 12, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0)),
                                                 (datetime.datetime(1900, 1, 1, 14, 0),
                                                  datetime.datetime(1900, 1, 1, 15, 0)),
                                                 (datetime.datetime(1900, 1, 1, 16, 0),
                                                  datetime.datetime(1900, 1, 1, 17, 0))],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 9, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 14, 0)),
                                                   (datetime.datetime(1900, 1, 1, 15, 0),
                                                    datetime.datetime(1900, 1, 1, 16, 0)),
                                                   (datetime.datetime(1900, 1, 1, 17, 0),
                                                    datetime.datetime(1900, 1, 1, 18, 0))],
                                     'available': []}},
              'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 9, 0)),
                                                   (datetime.datetime(1900, 1, 1, 10, 0),
                                                    datetime.datetime(1900, 1, 1, 11, 0)),
                                                   (datetime.datetime(1900, 1, 1, 12, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0)),
                                                   (datetime.datetime(1900, 1, 1, 14, 0),
                                                    datetime.datetime(1900, 1, 1, 15, 0)),
                                                   (datetime.datetime(1900, 1, 1, 16, 0),
                                                    datetime.datetime(1900, 1, 1, 17, 0))],
                                     'available': []}}}}
        assert sol == correct_sol

    def test_middle_overlap(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime

        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("5:00", "9:00")]}
                                       ]}]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "18:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 1}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)

        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 9, 0))],
                                       'available': [(datetime.datetime(1900, 1, 1, 9, 0),
                                                      datetime.datetime(1900, 1, 1, 18, 0))]}}},
 'resource': {'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 9, 0))],
                                     'available': [(datetime.datetime(1900, 1, 1, 5, 0),
                                                    datetime.datetime(1900, 1, 1, 8, 0))]}}}}

        assert sol == correct_sol

    def test_multiple_middle_overlap(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime

        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("5:00", "6:00"),("7:00", "8:00"),
                                                                     ("9:00", "10:00"),("11:00", "12:00"),
                                                                     ("13:00", "14:00"), ("15:00", "16:00")]}
                                       ]}]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("5:30", "6:30"),("7:30", "8:30"),
                                                                   ("9:30", "10:30"), ("11:30", "12:30"),
                                                                   ("13:30", "14:30"), ("15:30", "16:30"),
                                                                   ]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 1}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 5, 30),
                                                  datetime.datetime(1900, 1, 1, 6, 0)),
                                                 (datetime.datetime(1900, 1, 1, 7, 30),
                                                  datetime.datetime(1900, 1, 1, 8, 0)),
                                                 (datetime.datetime(1900, 1, 1, 9, 30),
                                                  datetime.datetime(1900, 1, 1, 10, 0)),
                                                 (datetime.datetime(1900, 1, 1, 11, 30),
                                                  datetime.datetime(1900, 1, 1, 12, 0)),
                                                 (datetime.datetime(1900, 1, 1, 13, 30),
                                                  datetime.datetime(1900, 1, 1, 14, 0)),
                                                 (datetime.datetime(1900, 1, 1, 15, 30),
                                                  datetime.datetime(1900, 1, 1, 16, 0))],
                                       'available': [(datetime.datetime(1900, 1, 1, 6, 0),
                                                      datetime.datetime(1900, 1, 1, 6, 30)),
                                                     (datetime.datetime(1900, 1, 1, 8, 0),
                                                      datetime.datetime(1900, 1, 1, 8, 30)),
                                                     (datetime.datetime(1900, 1, 1, 10, 0),
                                                      datetime.datetime(1900, 1, 1, 10, 30)),
                                                     (datetime.datetime(1900, 1, 1, 12, 0),
                                                      datetime.datetime(1900, 1, 1, 12, 30)),
                                                     (datetime.datetime(1900, 1, 1, 14, 0),
                                                      datetime.datetime(1900, 1, 1, 14, 30)),
                                                     (datetime.datetime(1900, 1, 1, 16, 0),
                                                      datetime.datetime(1900, 1, 1, 16, 30))]}}},
 'resource': {'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 5, 30),
                                                    datetime.datetime(1900, 1, 1, 6, 0)),
                                                   (datetime.datetime(1900, 1, 1, 7, 30),
                                                    datetime.datetime(1900, 1, 1, 8, 0)),
                                                   (datetime.datetime(1900, 1, 1, 9, 30),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 30),
                                                    datetime.datetime(1900, 1, 1, 12, 0)),
                                                   (datetime.datetime(1900, 1, 1, 13, 30),
                                                    datetime.datetime(1900, 1, 1, 14, 0)),
                                                   (datetime.datetime(1900, 1, 1, 15, 30),
                                                    datetime.datetime(1900, 1, 1, 16, 0))],
                                     'available': [(datetime.datetime(1900, 1, 1, 5, 0),
                                                    datetime.datetime(1900, 1, 1, 5, 30)),
                                                   (datetime.datetime(1900, 1, 1, 7, 0),
                                                    datetime.datetime(1900, 1, 1, 7, 30)),
                                                   (datetime.datetime(1900, 1, 1, 9, 0),
                                                    datetime.datetime(1900, 1, 1, 9, 30)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 11, 30)),
                                                   (datetime.datetime(1900, 1, 1, 13, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 30)),
                                                   (datetime.datetime(1900, 1, 1, 15, 0),
                                                    datetime.datetime(1900, 1, 1, 15, 30))]}}}}

        assert sol == correct_sol

    def test_resource_greater_than_demand(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("5:00", "12:00")]}
                                       ]}]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("7:14", "8:45")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 1}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 7, 14),
                                                          datetime.datetime(1900, 1, 1, 8, 45))],
                                               'available': []}}},
         'resource': {'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 7, 14),
                                                            datetime.datetime(1900, 1, 1, 8, 45))],
                                             'available': [(datetime.datetime(1900, 1, 1, 5, 0),
                                                            datetime.datetime(1900, 1, 1, 7, 14)),
                                                           (datetime.datetime(1900, 1, 1, 8, 45),
                                                            datetime.datetime(1900, 1, 1, 12, 0))]}}}}

        assert sol == correct_sol

    def test_two_resources_ends(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "12:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("7:00", "13:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("7:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 2,
                                                                2:"Diego"}]}]

        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 7, 0),
                                                  datetime.datetime(1900, 1, 1, 8, 0)),
                                                 (datetime.datetime(1900, 1, 1, 12, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0))],
                                       'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 12, 0))],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 7, 0),
                                                    datetime.datetime(1900, 1, 1, 8, 0)),
                                                   (datetime.datetime(1900, 1, 1, 12, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))],
                                     'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0))]}},
                        'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 12, 0))],
                                     'available': []}}}}

        assert sol == correct_sol

    def test_two_resouces_middle(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 2,
                                                                2: "Diego"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 10, 0),
                                                  datetime.datetime(1900, 1, 1, 11, 0))],
                                       'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 10, 0)),
                                                 (datetime.datetime(1900, 1, 1, 11, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0))],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 10, 0),
                                                    datetime.datetime(1900, 1, 1, 11, 0))],
                                     'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))]}},
                                    'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))],
                                     'available': []}}}}
        assert sol == correct_sol

    def test_three_resources(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("6:30", "11:30")]}
                                       ]},
                         {"key": "Sandra",
                          "schedule": [{"date": "3/1/2018", "time": [("5:00", "13:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("5:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)

        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 6, 30),
                                                  datetime.datetime(1900, 1, 1, 8, 0)),
                                                 (datetime.datetime(1900, 1, 1, 10, 0),
                                                  datetime.datetime(1900, 1, 1, 11, 30))],
                                       'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 10, 0))],
                                       'Sandra': [(datetime.datetime(1900, 1, 1, 5, 0),
                                                   datetime.datetime(1900, 1, 1, 6, 30)),
                                                  (datetime.datetime(1900, 1, 1, 11, 30),
                                                   datetime.datetime(1900, 1, 1, 13, 0))],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 6, 30),
                                                    datetime.datetime(1900, 1, 1, 8, 0)),
                                                   (datetime.datetime(1900, 1, 1, 10, 0),
                                                    datetime.datetime(1900, 1, 1, 11, 30))],
                                     'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0))]}},
              'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0))],
                                     'available': []}},
              'Sandra': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 5, 0),
                                                     datetime.datetime(1900, 1, 1, 6, 30)),
                                                    (datetime.datetime(1900, 1, 1, 11, 30),
                                                     datetime.datetime(1900, 1, 1, 13, 0))],
                                      'available': [(datetime.datetime(1900, 1, 1, 6, 30),
                                                     datetime.datetime(1900, 1, 1, 11, 30))]}}}}
        assert sol == correct_sol

    def test_mutliple_demands(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "16:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "9:00"),("10:00", "11:00")
                                                                   ,("12:00", "13:00"),("14:00", "15:00")]}
                                     ]},
                       {"key": "Nelligan",
                        "schedule": [{"date": "3/1/2018", "time": [("9:00", "10:00"),("11:00", "12:00")
                                                                   ,("13:00", "14:00"),("15:00", "16:00")]}
                                     ]}
                       ]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 1},
                                                               {"key": "Nelligan",
                                                                1: "Sally", "priority": 2, "num": 1}
                                                               ]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 9, 0)),
                                                 (datetime.datetime(1900, 1, 1, 10, 0),
                                                  datetime.datetime(1900, 1, 1, 11, 0)),
                                                 (datetime.datetime(1900, 1, 1, 12, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0)),
                                                 (datetime.datetime(1900, 1, 1, 14, 0),
                                                  datetime.datetime(1900, 1, 1, 15, 0))],
                                       'available': []}},
            'Nelligan': {'3/1/2018': {'Sally': [(datetime.datetime(1900, 1, 1, 9, 0),
                                                 datetime.datetime(1900, 1, 1, 10, 0)),
                                                (datetime.datetime(1900, 1, 1, 11, 0),
                                                 datetime.datetime(1900, 1, 1, 12, 0)),
                                                (datetime.datetime(1900, 1, 1, 13, 0),
                                                 datetime.datetime(1900, 1, 1, 14, 0)),
                                                (datetime.datetime(1900, 1, 1, 15, 0),
                                                 datetime.datetime(1900, 1, 1, 16, 0))],
                                      'available': []}}},
            'resource': {'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 9, 0)),
                                                   (datetime.datetime(1900, 1, 1, 10, 0),
                                                    datetime.datetime(1900, 1, 1, 11, 0)),
                                                   (datetime.datetime(1900, 1, 1, 12, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0)),
                                                   (datetime.datetime(1900, 1, 1, 14, 0),
                                                    datetime.datetime(1900, 1, 1, 15, 0))],
                                     'Nelligan': [(datetime.datetime(1900, 1, 1, 9, 0),
                                                   datetime.datetime(1900, 1, 1, 10, 0)),
                                                  (datetime.datetime(1900, 1, 1, 11, 0),
                                                   datetime.datetime(1900, 1, 1, 12, 0)),
                                                  (datetime.datetime(1900, 1, 1, 13, 0),
                                                   datetime.datetime(1900, 1, 1, 14, 0)),
                                                  (datetime.datetime(1900, 1, 1, 15, 0),
                                                   datetime.datetime(1900, 1, 1, 16, 0))],
                                     'available': []}}}}

        assert sol == correct_sol

    def test_second_non_overlapping(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00")]}
                                       ]},
                         {"key": "Sandra",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]

        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [],
                                       'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 10, 0)),
                                                 (datetime.datetime(1900, 1, 1, 11, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0))],
                                       'Sandra': [(datetime.datetime(1900, 1, 1, 10, 0),
                                                   datetime.datetime(1900, 1, 1, 11, 0))],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [],
                                     'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))]}},
              'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))],
                                     'available': []}},
              'Sandra': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 10, 0),
                                                     datetime.datetime(1900, 1, 1, 11, 0))],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 10, 0)),
                                                    (datetime.datetime(1900, 1, 1, 11, 0),
                                                     datetime.datetime(1900, 1, 1, 13, 0))]}}}}
        assert sol == correct_sol

    def test_three_overlap(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:15"), ("11:00", "13:00")]}
                                       ]},
                         {"key": "Sandra",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]

        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [(datetime.datetime(1900, 1, 1, 10, 0),
                                                  datetime.datetime(1900, 1, 1, 10, 15))],
                                       'Sally': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                  datetime.datetime(1900, 1, 1, 10, 0)),
                                                 (datetime.datetime(1900, 1, 1, 11, 0),
                                                  datetime.datetime(1900, 1, 1, 13, 0))],
                                       'Sandra': [(datetime.datetime(1900, 1, 1, 10, 15),
                                                   datetime.datetime(1900, 1, 1, 11, 0))],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 10, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 15))],
                                     'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))]}},
              'Sally': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                    datetime.datetime(1900, 1, 1, 10, 0)),
                                                   (datetime.datetime(1900, 1, 1, 11, 0),
                                                    datetime.datetime(1900, 1, 1, 13, 0))],
                                     'available': []}},
              'Sandra': {'3/1/2018': {'Montecute': [(datetime.datetime(1900, 1, 1, 10, 15),
                                                     datetime.datetime(1900, 1, 1, 11, 0))],
                                      'available': [(datetime.datetime(1900, 1, 1, 8, 0),
                                                     datetime.datetime(1900, 1, 1, 10, 15)),
                                                    (datetime.datetime(1900, 1, 1, 11, 0),
                                                     datetime.datetime(1900, 1, 1, 13, 0))]}}}}

        assert sol == correct_sol
    def test_three_overlap(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00"),
                                                                     ("14:00", "15:00"), ("16:00", "17:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("10:00", "11:00"), ("13:00", "14:00"),
                                                                     ("15:00", "16:00"), ("13:00", "14:00")]}
                                       ]},
                         {"key": "Sandra",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                       ]}
                         ]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)

