# from array import *

# Temp = [[11, 12, 5, 2], [15, 6,10,20], [10, 8, 12, 5], [12,15,8,6]]

# for r in Temp:
#    for c in r:
#       print(c,end = " ")
#    print()

"""o/p- 
11 12 5 2
15 6 10 20
10 8 12 5
12 15 8 6
"""

# print(Temp[0])

# print(Temp[1:3])

#Insert a value

# from array import *
# Temp = [[11, 12, 5, 2], [15, 6,10,20], [10, 8, 12, 5], [12,15,8,6]]

# Temp.insert(2, [5,11,13,6])

# for r in Temp:
#    for c in r:
#       print(c,end = " ")
#    print()

"""
o/p- 
11 12 5 2 
15 6 10 20
5 11 13 6
10 8 12 5
12 15 8 6

"""
# Update a value in array
# from array import *

# Temp = [[11, 12, 5, 2], [15, 6,10,20], [10, 8, 12, 5], [12,15,8,6]]

# Temp[2]= [20,30,40]
# Temp[1][0]= 5
# for r in Temp:
#    for c in r:
#       print(c,end = " ")
#    print()

"""
o/p- 
11 12 5 2 
5 6 10 20
20 30 40
12 15 8 6
"""

#Deleting the Values

from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()

'''
o/p- 
11 12 5 2 
15 6 10
10 8 12 5
'''