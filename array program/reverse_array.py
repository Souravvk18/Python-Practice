# program to reverse an array or string

#                                       method 1 , iterative way

# Function to reverse A[] from start to end

def reverse(A, start, end):
    while (start < end):
        A[start], A[end] = A[end], A[start]

        start += 1
        end -= 1

A =[10,20,30,40,50,60]
reverse(A, 0, 5)
print("the reverse list is:", A)

# the reverse list is: [60, 50, 40, 30, 20, 10]



#                   method 2, recursive way


def reverse(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverse(A, start+1, end-1)

A= [2,3,5,6,4,7]

reverse(A,0,9)
print("the reverse list is :", A)

# the reverse list is : [7, 4, 6, 5, 3, 2]

