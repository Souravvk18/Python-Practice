from array import *
arr =array('i',[10,20,30,40,50])
# for x in arr:
#    print(x)

"""
10
20
30
40
50"""

"""Accessing Array Element"""

# print(arr[2])
# print(arr[3]) 

"""
30
40
"""

"""Insertion Operation"""

from array import *
arr =[10,20,30,40,50]
arr.insert(2,100)
# for x in arr:
#     print(x)

"""
10
20
100
30
40
50
"""

"""Deletion Operation"""

# from array import *
# arr =[10,20,30,40,50]
# arr.remove(30)
# for x in arr:
#     print(x)

"""
10
20
40
50
"""

"""Search Operation"""

# from array import*
# arr = array('i', [10,20,30,40,50])
# print (arr.index(20))
# print(arr[3])

"""
1
40
"""

"""Update Operation"""

from array import *
arr = array('i', [10,20,30,40,50])
arr[2] = 80
for x in arr:
    print(x)
    
"""
10
20
80
40
50
"""
