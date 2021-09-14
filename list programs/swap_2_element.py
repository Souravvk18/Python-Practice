# program to swap two elements in a list

# def swap(list, pos1, pos2):
#     list[pos1], list[pos2]= list[pos2], list[pos1]
#     return list

# list = [10,20,30,40,50,60, 80, 90]
# pos1, pos2 = 0,3
# print( "the new list is:",swap(list, pos1, pos2))

"""the new list is: [40, 20, 30, 10, 50, 60]"""


# user input--
def swap(list, pos1, pos2):
    list[pos1], list[pos2]= list[pos2], list[pos1]
    return list

list = [10,20,30,40,50,60, 80, 90]
pos1= int(input("enter 1st value: "))
pos2= int(input("enter 2st value: "))
print( "the new list is:",swap(list, pos1, pos2))

"""
enter 1st value: 0
enter 2st value: 5
the new list is: [60, 20, 30, 40, 50, 10, 80, 90]
"""

