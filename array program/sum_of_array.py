
# method 1 --

# array=[10,20,30,40,50]
# arraysum= sum(array)

# print( "the sum of array is:",arraysum)

# the sum of array is: 150


# method 2--

def sum_array(arr):
    sum= 0
    for i in arr:
        sum = sum +i
    print("the sum is:", sum)

sum_array([10,20,30,40])

# the sum is: 100