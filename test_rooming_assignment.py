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
        correc_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/2/2018': {'Diego': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/3/2018': {'Diego': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/4/2018': {'Diego': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/5/2018': {'Diego': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []}},
            'Nelligan': {'3/1/2018': {'Sally': [('08:00', '12:00'),
                                                ('13:00', '18:00')],
                                      'available': []},
                         '3/2/2018': {'Sally': [('08:00', '12:00'),
                                                ('13:00', '18:00')],
                                      'available': []},
                         '3/3/2018': {'Sally': [('08:00', '12:00'),
                                                ('13:00', '18:00')],
                                      'available': []},
                         '3/4/2018': {'Sally': [('08:00', '12:00'),
                                                ('13:00', '18:00')],
                                      'available': []},
                         '3/5/2018': {'Sally': [('08:00', '12:00'),
                                                ('13:00', '18:00')],
                                      'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/2/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/3/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/4/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/5/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []}},
              'Sally': {'3/1/2018': {'Nelligan': [('08:00', '12:00'),
                                                  ('13:00', '18:00')],
                                     'available': []},
                        '3/2/2018': {'Nelligan': [('08:00', '12:00'),
                                                  ('13:00', '18:00')],
                                     'available': []},
                        '3/3/2018': {'Nelligan': [('08:00', '12:00'),
                                                  ('13:00', '18:00')],
                                     'available': []},
                        '3/4/2018': {'Nelligan': [('08:00', '12:00'),
                                                  ('13:00', '18:00')],
                                     'available': []},
                        '3/5/2018': {'Nelligan': [('08:00', '12:00'),
                                                  ('13:00', '18:00')],
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
                                       'available': [('08:00', '12:00'),
                                                     ('13:00', '18:00')]},
                          '3/2/2018': {'Diego': [],
                                       'available': [('08:00', '12:00'),
                                                     ('13:00', '18:00')]},
                          '3/3/2018': {'Diego': [],
                                       'available': [('08:00', '12:00'),
                                                     ('13:00', '18:00')]},
                          '3/4/2018': {'Diego': [],
                                       'available': [('08:00', '12:00'),
                                                     ('13:00', '18:00')]},
                          '3/5/2018': {'Diego': [],
                                       'available': [('08:00', '12:00'),
                                                     ('13:00', '18:00')]}},
            'Nelligan': {'3/1/2018': {'Sally': [],
                                      'available': [('08:00', '12:00'),
                                                    ('13:00', '18:00')]},
                         '3/2/2018': {'Sally': [],
                                      'available': [('08:00', '12:00'),
                                                    ('13:00', '18:00')]},
                         '3/3/2018': {'Sally': [],
                                      'available': [('08:00', '12:00'),
                                                    ('13:00', '18:00')]},
                         '3/4/2018': {'Sally': [],
                                      'available': [('08:00', '12:00'),
                                                    ('13:00', '18:00')]},
                         '3/5/2018': {'Sally': [],
                                      'available': [('08:00', '12:00'),
                                                    ('13:00', '18:00')]}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [],
                                     'available': [('01:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/2/2018': {'Montecute': [],
                                     'available': [('02:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/3/2018': {'Montecute': [],
                                     'available': [('01:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/4/2018': {'Montecute': [],
                                     'available': [('04:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/5/2018': {'Montecute': [],
                                     'available': [('01:00', '05:00'),
                                                   ('19:00', '22:00')]}},
              'Sally': {'3/1/2018': {'Nelligan': [],
                                     'available': [('01:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/2/2018': {'Nelligan': [],
                                     'available': [('01:00', '06:00'),
                                                   ('19:00', '22:00')]},
                        '3/3/2018': {'Nelligan': [],
                                     'available': [('04:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/4/2018': {'Nelligan': [],
                                     'available': [('02:00', '05:00'),
                                                   ('19:00', '22:00')]},
                        '3/5/2018': {'Nelligan': [],
                                     'available': [('01:00', '07:00'),
                                                   ('19:00', '22:00')]}}}}

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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/2/2018': {'Sally': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/3/2018': {'Sally': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/4/2018': {'Sally': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []},
                          '3/5/2018': {'Sally': [('08:00', '12:00'),
                                                 ('13:00', '18:00')],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'available': [('08:00', '12:00'),
                                                   ('13:00', '18:00')]},
                        '3/2/2018': {'available': [('08:00', '12:00'),
                                                   ('13:00', '18:00')]},
                        '3/3/2018': {'available': [('08:00', '12:00'),
                                                   ('13:00', '18:00')]},
                        '3/4/2018': {'available': [('08:00', '12:00'),
                                                   ('13:00', '18:00')]},
                        '3/5/2018': {'available': [('08:00', '12:00'),
                                                   ('13:00', '18:00')]}},
              'Sally': {'3/1/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/2/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/3/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/4/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
                                     'available': []},
                        '3/5/2018': {'Montecute': [('08:00', '12:00'),
                                                   ('13:00', '18:00')],
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [('08:00', '09:00'),
                                                 ('10:00', '11:00'),
                                                 ('12:00', '13:00'),
                                                 ('14:00', '15:00'),
                                                 ('16:00', '17:00')],
                                       'available': [('09:00', '10:00'),
                                                     ('11:00', '12:00'),
                                                     ('13:00', '14:00'),
                                                     ('15:00', '16:00'),
                                                     ('17:00', '18:00')]}}},
 'resource': {'Sally': {'3/1/2018': {'Montecute': [('08:00', '09:00'),
                                                   ('10:00', '11:00'),
                                                   ('12:00', '13:00'),
                                                   ('14:00', '15:00'),
                                                   ('16:00', '17:00')],
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('09:00', '10:00'),
                                                 ('11:00', '12:00'),
                                                 ('13:00', '14:00'),
                                                 ('15:00', '16:00'),
                                                 ('17:00', '18:00')],
                                       'Sally': [('08:00', '09:00'),
                                                 ('10:00', '11:00'),
                                                 ('12:00', '13:00'),
                                                 ('14:00', '15:00'),
                                                 ('16:00', '17:00')],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [('09:00', '10:00'),
                                                   ('11:00', '12:00'),
                                                   ('13:00', '14:00'),
                                                   ('15:00', '16:00'),
                                                   ('17:00', '18:00')],
                                     'available': []}},
              'Sally': {'3/1/2018': {'Montecute': [('08:00', '09:00'),
                                                   ('10:00', '11:00'),
                                                   ('12:00', '13:00'),
                                                   ('14:00', '15:00'),
                                                   ('16:00', '17:00')],
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

        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [('08:00', '09:00')],
                                       'available': [('09:00', '18:00')]}}},
                        'resource': {'Sally': {'3/1/2018': {'Montecute': [('08:00', '09:00')],
                                     'available': [('05:00', '08:00')]}}}}


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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [('05:30', '06:00'),
                                                 ('07:30', '08:00'),
                                                 ('09:30', '10:00'),
                                                 ('11:30', '12:00'),
                                                 ('13:30', '14:00'),
                                                 ('15:30', '16:00')],
                                       'available': [('06:00', '06:30'),
                                                     ('08:00', '08:30'),
                                                     ('10:00', '10:30'),
                                                     ('12:00', '12:30'),
                                                     ('14:00', '14:30'),
                                                     ('16:00', '16:30')]}}},
 'resource': {'Sally': {'3/1/2018': {'Montecute': [('05:30', '06:00'),
                                                   ('07:30', '08:00'),
                                                   ('09:30', '10:00'),
                                                   ('11:30', '12:00'),
                                                   ('13:30', '14:00'),
                                                   ('15:30', '16:00')],
                                     'available': [('05:00', '05:30'),
                                                   ('07:00', '07:30'),
                                                   ('09:00', '09:30'),
                                                   ('11:00', '11:30'),
                                                   ('13:00', '13:30'),
                                                   ('15:00', '15:30')]}}}}

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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [('07:14', '08:45')],
                                       'available': []}}},
                        'resource': {'Sally': {'3/1/2018': {'Montecute': [('07:14', '08:45')],
                                     'available': [('05:00', '07:14'),
                                                   ('08:45', '12:00')]}}}}

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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('07:00', '08:00'),
                                                 ('12:00', '13:00')],
                                       'Sally': [('08:00', '12:00')],
                                       'available': []}}},
                    'resource': {'Diego': {'3/1/2018': {'Montecute': [('07:00', '08:00'),
                                                   ('12:00', '13:00')],
                                     'available': [('08:00', '12:00')]}},
              'Sally': {'3/1/2018': {'Montecute': [('08:00', '12:00')],
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('10:00', '11:00')],
                                       'Sally': [('08:00', '10:00'),
                                                 ('11:00', '13:00')],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [('10:00', '11:00')],
                                     'available': [('08:00', '10:00'),
                                                   ('11:00', '13:00')]}},
              'Sally': {'3/1/2018': {'Montecute': [('08:00', '10:00'),
                                                   ('11:00', '13:00')],
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

        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('06:30', '08:00'),
                                                 ('10:00', '11:30')],
                                       'Sally': [('08:00', '10:00')],
                                       'Sandra': [('05:00', '06:30'),
                                                  ('11:30', '13:00')],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [('06:30', '08:00'),
                                                   ('10:00', '11:30')],
                                     'available': [('08:00', '10:00')]}},
                                    'Sally': {'3/1/2018': {'Montecute': [('08:00', '10:00')],
                                     'available': []}},
                                    'Sandra': {'3/1/2018': {'Montecute': [('05:00', '06:30'),
                                                    ('11:30', '13:00')],
                                      'available': [('06:30', '11:30')]}}}}
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Sally': [('08:00', '09:00'),
                                                 ('10:00', '11:00'),
                                                 ('12:00', '13:00'),
                                                 ('14:00', '15:00')],
                                       'available': []}},
                                    'Nelligan': {'3/1/2018': {'Sally': [('09:00', '10:00'),
                                                ('11:00', '12:00'),
                                                ('13:00', '14:00'),
                                                ('15:00', '16:00')],
                                      'available': []}}},
                        'resource': {'Sally': {'3/1/2018': {'Montecute': [('08:00', '09:00'),
                                                   ('10:00', '11:00'),
                                                   ('12:00', '13:00'),
                                                   ('14:00', '15:00')],
                                     'Nelligan': [('09:00', '10:00'),
                                                  ('11:00', '12:00'),
                                                  ('13:00', '14:00'),
                                                  ('15:00', '16:00')],
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
                                       'Sally': [('08:00', '10:00'),
                                                 ('11:00', '13:00')],
                                       'Sandra': [('10:00', '11:00')],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [],
                                     'available': [('08:00', '10:00'),
                                                   ('11:00', '13:00')]}},
              'Sally': {'3/1/2018': {'Montecute': [('08:00', '10:00'),
                                                   ('11:00', '13:00')],
                                     'available': []}},
              'Sandra': {'3/1/2018': {'Montecute': [('10:00', '11:00')],
                                      'available': [('08:00', '10:00'),
                                                    ('11:00', '13:00')]}}}}

        assert sol == correct_sol

    def test_three_overlap_first(self):
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('10:00', '10:15')],
                                       'Sally': [('08:00', '10:00'),
                                                 ('11:00', '13:00')],
                                       'Sandra': [('10:15', '11:00')],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [('10:00', '10:15')],
                                     'available': [('08:00', '10:00'),
                                                   ('11:00', '13:00')]}},
                            'Sally': {'3/1/2018': {'Montecute': [('08:00', '10:00'),
                                                   ('11:00', '13:00')],
                                     'available': []}},
                            'Sandra': {'3/1/2018': {'Montecute': [('10:15', '11:00')],
                                      'available': [('08:00', '10:15'),
                                                    ('11:00', '13:00')]}}}}


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
                                                                     ("15:00", "11:00"), ("13:00", "14:00")]}
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
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('10:00', '11:00')],
                                       'Sally': [('08:00', '10:00'),
                                                 ('11:00', '13:00')],
                                       'available': []}}},
 'resource': {'Diego': {'3/1/2018': {'Montecute': [('10:00', '11:00')],
                                     'available': [('13:00', '14:00'),
                                                   ('13:00', '14:00'),
                                                   ('15:00', '11:00')]}},
              'Sally': {'3/1/2018': {'Montecute': [('08:00', '10:00'),
                                                   ('11:00', '13:00')],
                                     'available': [('14:00', '15:00'),
                                                   ('16:00', '17:00')]}},
              'Sandra': {'3/1/2018': {'available': [('08:00', '13:00')]}}}}


        assert sol == correct_sol


# Test with invalid input
class TestSolveWrongInput(TestCase):

    def test_missing_resource(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00"),
                                                                     ("14:00", "15:00"), ("16:00", "17:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("10:00", "11:00"), ("13:00", "14:00"),
                                                                     ("15:00", "17:00")]}
                                       ]}]
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'Diego': [('10:00', '11:00')],
                                       'Sally': [('08:00', '10:00'),
                                                 ('11:00', '13:00')],
                                       'available': []}}},
                        'resource': {'Diego': {'3/1/2018': {'Montecute': [('10:00', '11:00')],
                                     'available': [('13:00', '14:00'),
                                                   ('15:00', '17:00')]}},
                                    'Sally': {'3/1/2018': {'Montecute': [('08:00', '10:00'),
                                                   ('11:00', '13:00')],
                                     'available': [('14:00', '15:00'),
                                                   ('16:00', '17:00')]}}}}
        assert sol == correct_sol

    def test_no_resource(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = []
        demand_info = [{"key": "Montecute",
                        "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                     ]}]
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {'Montecute': {'3/1/2018': {'available': [('08:00', '13:00')]}}},
                         'resource': {}}
        assert sol == correct_sol

    def test_no_demand(self):
        from rooming_assignments import solve_demand_resource_schedule
        import datetime
        resource_info = [{"key": "Sally",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "10:00"), ("11:00", "13:00"),
                                                                     ("14:00", "15:00"), ("16:00", "17:00")]}
                                       ]},
                         {"key": "Diego",
                          "schedule": [{"date": "3/1/2018", "time": [("10:00", "11:00"), ("13:00", "14:00"),
                                                                     ("15:00", "11:00"), ("13:00", "14:00")]}
                                       ]},
                         {"key": "Sandra",
                          "schedule": [{"date": "3/1/2018", "time": [("8:00", "13:00")]}
                                       ]}
                         ]
        demand_info = []
        instructions = [{"key": "mapping", "order": 1, "map": [{"key": "Montecute",
                                                                1: "Sally", "priority": 1, "num": 3,
                                                                2: "Diego",
                                                                3: "Sandra"}]}]
        sol = solve_demand_resource_schedule(demand_info, resource_info, instructions)
        correct_sol = {'demand': {},
                        'resource': {'Diego': {'3/1/2018': {'available': [('10:00', '11:00'),
                                                   ('13:00', '14:00'),
                                                   ('13:00', '14:00'),
                                                   ('15:00', '11:00')]}},
                            'Sally': {'3/1/2018': {'available': [('08:00', '10:00'),
                                                   ('11:00', '13:00'),
                                                   ('14:00', '15:00'),
                                                   ('16:00', '17:00')]}},
                            'Sandra': {'3/1/2018': {'available': [('08:00', '13:00')]}}}}
        assert sol == correct_sol