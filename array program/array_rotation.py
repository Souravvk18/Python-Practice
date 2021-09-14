# Rotation of the above array by 2--

# method 1--(using temp array)

# def rotate(arr, n , d):
#     temp= []
#     i=0
#     while (i<d):
#         temp.append(arr[i])
#         i= i+1
#     i= 0
#     while (d<n):
#         arr[i] = arr[d]
#         i= i+1
#         d= d+1
#     arr[ : ] = arr[ 0 : i] + temp
#     return arr
# arr=[8,9,3,4,5,6,7]
# print("array after the rotation is:")
# print(rotate(arr, len(arr), 2))

"""array after the rotation is:
[3, 4, 5, 6, 7, 8, 9]"""


# method 2--- list slicing

# def rotation(arr, n, d):
#     arr [:] = arr[d :n] + arr[0 : d]
#     return arr

# arr=[8,9,10,3,4,5,6,7]
# print("array after the rotation is:")
# print(rotation(arr, len(arr), 3))

"""
array after the rotation is:
[3, 4, 5, 6, 7, 8, 9, 10]
"""

arr=[8,9,10,3,4,5,6,7]
print(arr[3:8])

