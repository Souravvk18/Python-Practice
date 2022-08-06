list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print ("list1[0]: ", list1[0])
# print ("list2[1:5]: ", list2[1:5])

"""
accessing value:

list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
"""

"insert values"

list = ['physics', 'chemistry', 1997, 2000]
list.insert(2,1990)
print(list)

"""
['physics', 'chemistry', 1990, 1997, 2000]
"""


"Update list value"

# list = ['physics', 'chemistry', 1997, 2000]
# list[2]= 1998

# list[1]= 'math'

# print(list)

"""
['physics', 'chemistry', 1998, 2000]

['physics', 'math', 1998, 2000]
"""


"""delete from list"""

list = ['physics', 'chemistry', 1997, 2000]

# del list[1]
# print(list)

# del list[3]
# print(list)

"""
['physics', 1997, 2000]

['physics', 'chemistry', 1997]
"""