# Program to find largest element in an array

# method 1--

# def largest(arr):
#     max = arr[0]

#     for i in range(1, len(arr)):
#         if arr[i] > max:
#             max =arr[i]
#     print("largest number is:", max)

# largest([10,20,50,40,30])

# o/p-  largest number is: 50



# method 2--

arr= [10,40,50, 20, 70]
max=arr[0]
for i in range(1,len(arr)):
    if arr[i] > max:
        max =arr[i]
print("largest number is:", max)

# o/p-  largest number is: 70