# method 1   one line solution

def factorial(n):
    return 1 if(n==0 or n==1) else n * factorial(n-1)
num = 5
# print("the factorial of" ,num, "is:",factorial(num))

# the factorial of 5 is: 120


#                                               method 2 - iterative
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact =1
        while(n>1):
            fact *= n
            n -= 1
        return fact
# print(factorial(6))  # input given

n= int(input("enter the number:"))   # user input
print(factorial(n))

""" 
enter the number:4
24
"""
