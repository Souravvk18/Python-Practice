# program to find second largest number in a list

# list = [10,30,40,20,25]

# list.sort()
# print("2nd smallest is:", list[-2])

# method - 2--

def findLargest(arr):
    secondLargest =arr[0]
    largest = arr[0]
    for i in range(len(arr)):
         if arr[i] > largest:
             largest= arr[i]

    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]

    return secondLargest
arr = [ 10,60,50,25,70]

print("the second largest number is: ", findLargest(arr))

"""
the second largest number is:  60
"""
