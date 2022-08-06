Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
# print(Days)
# print(Months)
# print(Dates)

"""
{'Mon', 'Wed', 'Tue', 'Sun', 'Thu', 'Sat', 'Fri'}
{'Jan', 'Feb', 'Mar'}
{17, 21, 22}
"""

# for d in Days:
#     print(d)

"""
Wed
Mon
Sun
Thu
Fri
Sat
Tue
"""

"""Adds value to a set"""

Day=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
# Day.add("Sun")
# print(Day)

"""{'Mon', 'Thu', 'Tue', 'Sat', 'Fri', 'Sun', 'Wed'}"""

"""remove value to a set"""

Day.discard("Mon")
# print(Day)

"""{'Fri', 'Wed', 'Tue', 'Sat', 'Thu'}"""


"""Union of Sets"""

# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays = DaysA|DaysB
# print(AllDays)

"""{'Fri', 'Sun', 'Sat', 'Thu', 'Mon', 'Wed', 'Tue'}"""


"""Intersection of Sets :- The intersection operation on two sets produces a new set containing only
 the common elements from both the sets."""

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
# print(AllDays)

"""{'Wed'}"""

"""Difference of Sets :- The difference operation on two sets produces a new set containing only the elements
 from the first set and none from the second set."""

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
# print(AllDays)

"""{'Mon', 'Tue'}"""

"""Compare Sets :- We can check, if a given set is a subset or superset of another set.
 The result is True or False depending on the elements present in the sets."""

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)


"""
True
True"""


