# Maximum and minimum of an array

#                                METHOD 1 (Simple Linear Search) 

# class pair:
#     def __init__(self):
#         self.max= 0
#         self.min= 0
    
# def getMinMax(arr:list, n:int) ->pair:
#     minmax  = pair()

#     if n==1:
#         minmax.max= arr[0]
#         minmax.min = arr[0]
#         return minmax

#     if arr[0] > arr[1]:
#         minmax.min= arr[1]
#         minmax.max =arr[0]
#     else:
#         minmax.max = arr[1]
#         minmax.min= arr[0]

#     for i in range(2,n):
#         if arr[i] > minmax.max:
#             minmax.max = arr[i]
#         elif arr[i] < minmax.min:
#             minmax.min = arr[i]
#     return minmax

# if __name__ == "__main__":
#     arr =[100, 500, 50, 3000, 200]
#     arr_size = 5
#     minmax = getMinMax(arr, 5)

#    print("minimum element is:", minmax.min)
#    print("maximum element is:", minmax.max)

"""
minimum element is: 50
maximum element is: 3000
"""


#                       METHOD 2 (Compare in Pairs) 

def getMinMax(arr):
    n = len(arr)

    if(n % 2==0):
        mx =max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i =2
    else:
        mx = mn = arr[0]
        i =1

    while (i < n-1):
        if arr[i] < arr[i+1]:
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])

        else:
            mx = max(mx, arr[i])
            mn = min (mn, arr[i+1])

        i += 2
    return (mx, mn)

if __name__ == "__main__":
    arr = [ 100, 10, 1000, 3000, 2500, 5000]
    mx, mn = getMinMax(arr)

    print("The minimum vlue is:", mn)
    print("The maximum vlue is:", mx)


"""The minimum vlue is: 10
The maximum vlue is: 5000"""
