# Program to Split the array and add the first part to the end

def split_array(arr, n ,k):
    b =arr[: k]
    return (arr[k ::] + b[::])

arr =[10,5,20,30,25, 40]
print(split_array(arr, len(arr), 2))

"""[20, 30, 25, 40, 10, 5]"""



# def split_array(arr, n ,k):
#     b =arr[: k]
#     return (arr[k ::] + b[::])

# arr =[10,5,20,30,25, 40, 50]
# n = len(arr)
# position = 3

# print(split_array(arr, n, position))
"""[30, 25, 40, 50, 10, 5, 20]"""


# to print one by one.

# arr = split_array(arr, n, position)
# for i in range(0,n):
#     print(arr[i])

"""
30
25
40
50
10
5
20"""

"""[30, 25, 40, 50, 10, 5, 20]"""
