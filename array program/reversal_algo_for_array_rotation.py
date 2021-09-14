def reverse(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start]= arr[end]
        arr[end] = temp
        start = start +1 
        end = end -1
def leftRotate(arr, d):
    n = len(arr)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)


# def array(arr):
#     for i in range(0,len(arr)):
#         print(arr[i])

arr =[1,2,3,4,5,6,7]
leftRotate(arr,2)
print(arr)
# array(arr)

"""[3, 4, 5, 6, 7, 1, 2]"""