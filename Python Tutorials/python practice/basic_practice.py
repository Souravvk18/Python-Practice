"""1. Python program to add two numbers"""

# num1= 20
# num2 = 30
# sum = num1+num2
# print("The sum of num1 & num2 is:",sum)

"""The sum of num1 & num2 is: 50"""

                                                # after taking user input

# num1=input("enter the 1st number:")
# num2=input("Enter the 2nd number:")

# sum = int(num1) + int(num2)
# print(sum)
# print("the sum of {} and {} is {}".format(num1,num2,sum))

"""
enter the 1st number:20
Enter the 2nd number:30
the sum of 20 and 30 is 50
"""


""" 2. Python Program for factorial of a number """ 

#recursive method:-

def factorial(n):
     return 1 if (n==0 or n==1) else n * factorial(n-1)

num = 5
# num = int(input("enter the value:")) #user input 
# print("The factorial is:", factorial(num))


"""The factorial is: 120

enter the value:10
The factorial is: 3628800
"""

#Iterative method:-

# def factorial(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#         fact= 1
#         while(n>0):
#             fact *= n
#             n -= 1
#         return fact

# # num = 6
# num = int(input("enter the value:"))
# print("the factoral is:", factorial(num))

"""the factoral is: 720

enter the value:4
the factoral is: 24
"""

"""3. Python Program for simple interest"""

                                            # user input 
# p= int(input("enter the amount:"))
# t= int(input("enter the time:"))
# r= int(input("enter the interest:"))
# si=(p*t*r)/ 100
# print(si)

"""
enter the amount:1000
enter the time:5
enter the interest:10
500.0
"""
# input given

# def interest(p,t,r):
#     print("the principle is:", p)
#     print("the time is:", t)
#     print("the interest rate is:", r)

#     si= (p*t*r)/100
#     print("the interest is:", si)
#     return si
# interest(1000,5,10)

"""the interest is: 500.0

the principle is: 1000
the time is: 5
the interest rate is: 10
the interest is: 500.0"""


""" 4. Maximum of two numbers in Python"""
#1st method

# def maximum(a,b):
#     if a > b:
#         print(" the bigger number is", a)
#     else:
#         print("the bigger number is", b)
# maximum(10,20)
# maximum(50,20)

"""
the bigger number is 20
 the bigger number is 50
 """

# 2nd method

# a = 20
# b= 30
# if a>b:
#     print(" the bigger number is", a)
# else:
#     print("the bigger number is", b)

""" the bigger number is 30"""
# 3rd method

# def maximum(a, b):
     
#     if a >= b:
#         return a
#     else:
#         return b
# a = 2
# b = 4
# print(maximum(a, b))

# method 4 

# a = int(input("enter the 1st value: "))
# b = int(input("enter the 2nd value: "))
# maximum = max(a, b)
# print( "the max value is :", maximum)

"""enter the 1st value: 100
enter the 2nd value: 500
the max value is : 500"""


""" 5. Python Program for compound interest  [A = P(1 + R/100)^t] """

def interest(p, r, t):

    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print("Compound interest is", CI)
 
# interest(10000, 10, 2)
interest(1000, 8, 5)


""" Compound interest is 2100.000000000002

Compound interest is 469.32807680000064"""
