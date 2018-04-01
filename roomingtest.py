import rooming_assignments as ra


given_rules = [{"key": "mapping", "order": 1, "map": [{"key": "Nelligan", 1: "Sally", "priority": 1, "num": 1},
                                                         {"key": "Montecute", 1: "Diego", "priority": 2, "num": 1}]}]


x = ra.MappingRule(given_rules[0]["map"])

y = ra.Instructions(given_rules)
print(x.demand_to_resources_by_resource_priority)
print(y.mapping.demand_to_resources_by_resource_priority)

print(x.get_resources_for_demand_ordered_by_priority("Nelligan"))



resource_info = [{"key": "Sally",
                  "schedule": [{"date": "3/1/2018", "time": [("8:00", "12:00"),("13:00", "18:00")]},
                 {"date": "3/2/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                 {"date": "3/3/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                 {"date": "3/4/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]},
                 {"date": "3/5/2018", "time": [("8:00", "12:00"), ("13:00", "18:00")]}
                  ]},
                 {"key": "Diego",
                  "schedule": [{"date": "3/1/2018","time": [("8:00", "12:00"), ("13:00","18:00")]},
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

#priority, what order should the preferences be done in.
given_rules = [{"key"      :"mapping",
          "order" : 1,
          "map"      : [{"key": "Nelligan", 1: "Sally","priority": 1,"num": 1},
                        {"key": "Montecute", 1: "Diego","priority": 2,"num": 1}]},
       ]

print(ra.solveDemandResourceSchedule(demand_info, resource_info, given_rules))

x = ra.solveDemandResourceSchedule(demand_info, resource_info, given_rules)
print(len(ra.solveDemandResourceSchedule(demand_info, resource_info, given_rules)))

for physician, dates_assignments in x.items():
    print(physician)
    for date, schedule in dates_assignments.items():
        print("\t {}".format(date))
        for assignment, segments in schedule.items():
            print("\t\t assignment= {} times={}".format(assignment, segments))


#
# def find_overlap(t1, t2):
#     segment1 = t1[0]
#     segment2 = t2[0]
#
#     if segment1[1] < segment2[0]:
#
#         #no overlap,so remover trailing from list1 and add to to available
#         t1.pop(0)
#         return [segment1], [], []
#     if segment2[1] < segment1[0]:
#         # no overlap and segment2 is trailing
#         t2.pop(0)
#         return [], [segment2], []
#
#     overlap = (max(segment1[0],segment2[0]), min(segment1[1], segment2[1]))
#
#     #now we have to figure out how to update available time, both for
#     #case 1: they are exactly same segment
#     if segment1[0] == overlap[0] and segment1[1] == overlap[1] and segment1[0] == overlap[0] and segment2[1] == overlap[1]:
#
#         t1.pop(0)
#         t2.pop(0)
#
#         return [], [], [overlap]
#
#     #case2: they start same time, but 1 is ends later  than other
#
#     if segment1[0] == overlap[0] and segment2[0] == overlap[0] and segment1[1] != overlap[1] or segment2[1] != overlap[1]:
#
#         if segment1[1] > segment2[1]:
#
#             t2.pop(0)
#             t1.pop(0)
#
#             t1.insert(0,(overlap[1], segment1[1]))
#
#             return [], [], [overlap]
#         else:
#             t2.pop(0)
#             t1.pop(0)
#
#             t2.insert(0, (overlap[1], segment2[1]))
#
#             return [], [], [overlap]
#
#     #case3: they end same time, but 1 is starts sooner than other
#     if segment1[1] == overlap[1] and segment2[1] == overlap[1] and segment1[0] != overlap[0] or segment2[0] != overlap[1]:
#
#         if segment1[0] < segment2[0]:
#
#             t1.pop(0)
#             t2.pop(0)
#
#             return [(segment1[0], overlap[0])], [],[overlap]
#
#         else:
#             t1.pop(0)
#             t2.pop(0)
#
#             return [], [(segment2[0], overlap[0])], [overlap]
#     #case4: one is starts sooner and ends later, completely overlapping one
#
#     if segment1[0]> segment2[0] and segment1[1] < segment2[1]:
#
#         t1.pop()
#         t2.pop()
#
#         t2.insert(0, (overlap[1], segment2[1]))
#
#         return [], [(segment2[0],overlap[0])], [overlap]
#
#     if segment2[0] > segment1[0] and segment2[1] < segment1[1]:
#         t1.pop()
#         t2.pop()
#
#         t1.insert(0, (overlap[1], segment1[1]))
#
#         return [(segment1[0], overlap[0])],[], [overlap]
#
#     #case 5: segments do not either start together or end together, but overlap. like a random middle segemnt
#
#     if segment1[1] > segment2[1]:
#         t1.pop()
#         t2.pop()
#
#         t1.insert(0, (overlap[1], segment1[1]))
#
#         return [], [(segment2[0],overlap[0])], [overlap]
#
#     if segment2[1] > segment1[1]:
#         t1.pop()
#         t2.pop()
#
#         t2.insert(0, (overlap[1], segment2[1]))
#
#         return [(segment1[0], overlap[0])],[], [overlap]
#
#     assert("Should have not gotten here")
#
#
#
# #Completely overlapping
# t1 = [(3,5), (6,9)]
# t2 = [(3,5), (6,9)]
# t1_result = []
# t2_result = []
# overlap_result = []
#
# right_t1 = []
# right_t2 = []
# overlap_right = [(3,5), (6,9)]
#
# while(len(t1) > 0 and len(t2) > 0):
#
#     t1_trailing, t2_trailing, overlap_add = find_overlap(t1, t2)
#
#     t1_result += t1_trailing
#     t2_result += t2_trailing
#     overlap_result += overlap_add
#
#
# assert right_t1 == t1_result
# assert right_t2 == t2_result
# assert overlap_result == overlap_right
#
# #Completley non-overlapping
#
# t1 = [(1,3), (6,9)]
# t2 = [(4,5), (10,12)]
#
# t1_result = []
# t2_result = []
# overlap_result = []
#
# right_t1 = [(1, 3), (6, 9)]
# right_t2 = [(4, 5), (10, 12)]
# overlap_right = []
#
# while(len(t1) > 0 and len(t2) > 0):
#
#     t1_trailing, t2_trailing, overlap_add = find_overlap(t1, t2)
#
#     t1_result += t1_trailing
#     t2_result += t2_trailing
#     overlap_result += overlap_add
#
#     if len(t1) == 0 and len(t2) != 0:
#         t2_result += t2
#
#     if len(t2) == 0 and len(t1) != 0:
#         t1_result += t1
#
#
# assert right_t1 == t1_result
# assert right_t2 == t2_result
# assert overlap_result == overlap_right
#
#
#
# #Todo: finish last two test
# #segment overlaps with a leading segment 1
#
# t1 = [(1, 5)]
# t2 = [(1, 10)]
# t1_result = []
# t2_result = []
# overlap_result = []
#
# right_t1 = []
# right_t2 = [(5, 10)]
# overlap_right = [(1,5)]
#
# while(len(t1) > 0 and len(t2) > 0):
#
#     t1_trailing, t2_trailing, overlap_add = find_overlap(t1, t2)
#
#     t1_result += t1_trailing
#     t2_result += t2_trailing
#     overlap_result += overlap_add
#
#     if len(t1) == 0 and len(t2) != 0:
#         t2_result += t2
#
#     if len(t2) == 0 and len(t1) != 0:
#         t1_result += t1
#
# print(t1_result)
# print(t2_result)
# print(overlap_result)
#
# assert right_t1 == t1_result
# assert right_t2 == t2_result
# assert overlap_result == overlap_right
#
# #reverse
#
# t1 = [(1, 10)]
# t2 = [(1, 5)]
# t1_result = []
# t2_result = []
# overlap_result = []
#
# right_t1 = [(5, 10)]
# right_t2 = []
# overlap = [(1,5)]
#
#
# while(len(t1) > 0 and len(t2) > 0):
#
#     t1_trailing, t2_trailing, overlap_add = find_overlap(t1, t2)
#
#     t1_result += t1_trailing
#     t2_result += t2_trailing
#     overlap_result += overlap_add
#
#     if len(t1) == 0 and len(t2) != 0:
#         t2_result += t2
#
#     if len(t2) == 0 and len(t1) != 0:
#         t1_result += t1
#
# print(t1_result)
# print(t2_result)
# print(overlap_result)
#
# assert right_t1 == t1_result
# assert right_t2 == t2_result
# assert overlap_result == overlap_right
#
# #reverse
#
