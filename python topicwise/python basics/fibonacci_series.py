# method -1   using array  [ F(n) = f(n-1) + f(n-2)]

"""Python Program for n-th Fibonacci number"""

def fibonacci(n):
    if n<=0:
        return "incorrect inputs !"
    data =[0,1]
    if n >2:
        for i in range(2,n):
            data.append(data[i-1] + data[i-2])
        else:
            return data[n-1]
    
print(fibonacci(9))  #o/p- 21
# print(fibonacci(10))  #o/p- 34


# method 2 using recursion

# def fibonacci(n):
#     if n<= 0:
#         return "incorrect input"
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

# # taking user input

# num = int(input("enter the number: "))
# print(fibonacci(num))

"""
34

enter the number: 11
55
"""






