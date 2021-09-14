# program to find smallest number in a list

# list=[10,5,20,15,25]
# small= min(list)
# print("the small number is :", small)


# o/p-  the small number is : 5



# list=[10,5,20,15,25]
# list=[100,50,20,15,25]
# list.sort()
# print(list)
# print("the small number is :", list[0])

"""
[15, 20, 25, 50, 100]

 the small number is : 5
the small number is : 15"""

# without inbuilt function.

# def mymin(list):
#     min =list[0]
#     for i in list:
#         if min > i:
#             min =i
#     return min

# list =[10,5,40,20,15]
# print("the min number is:", mymin(list))

"""the min number is: 5"""



# program to find largest number in a list

# list=[10,5,20,15,25]
# large= max(list)
# print("the large number is :", large)

"""the large number is : 25"""



# list=[10,5,20,15,25]
# list=[100,50,20,15,25]
# list.sort()
# print(list)
# print("the small number is :", list[-1])

"""[15, 20, 25, 50, 100]
the small number is : 100"""


# without inbuilt function.

def mymax(list):
    max =list[0]
    for i in list:
        if i > max:
            max = i
    return max

list =[10,5,80,20,15]
print("the max number is:", mymax(list))

""" the max number is: 80"""



