import rooming_assignments as ra


given_rules = [{"key": "mapping", "priority": 1, "map": [{"key": "Nelligan", 1: "Sally", "priority": 1, "num": 1},
                                                         {"key": "Montecute", 1: "Diego", "priority": 2, "num": 1}]}]


x = ra.MappingRule(given_rules[0]["map"])

y = ra.Rules(given_rules)
print(x.demand_to_resources)
print(y.mapping_rule.demand_to_resources)

print(x.get_resources_for_demand_by_priority("Nelligan"))



resource_info = [{"key": "Sally",
                  "schedule":[{"date":"3/1/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/2/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/3/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/4/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/5/2018","time":[("8:00","12:00"),("13:00","18:00")]}
                  ]},
                 {"key": "Diego",
                  "schedule":[{"date":"3/1/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/2/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/3/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/4/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/5/2018","time":[("8:00","12:00"),("13:00","18:00")]}
                  ]}]
demand_info = [{"key": "Montecute",
                  "schedule":[{"date":"3/1/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/2/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/3/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/4/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/5/2018","time":[("8:00","12:00"),("13:00","18:00")]}
                  ]},
                 {"key": "Nelligan",
                  "schedule":[{"date":"3/1/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/2/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/3/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/4/2018","time":[("8:00","12:00"),("13:00","18:00")]},
                 {"date":"3/5/2018","time":[("8:00","12:00"),("13:00","18:00")]}
                  ]}]

#priority, what order should the preferences be done in.
given_rules = [{"key"      :"mapping",
          "priority" : 1,
          "map"      : [{"key":"Nelligan", 1:"Sally","priority":1,"num":1},
                        {"key":"Montecute", 1:"Diego","priority":2,"num":1}]},
       ]

print(ra.solveDemandResourceSchedule(demand_info, resource_info, given_rules))

print(len(ra.solveDemandResourceSchedule(demand_info, resource_info, given_rules)))