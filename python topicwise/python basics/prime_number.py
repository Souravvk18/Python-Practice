# to check a number is prime or not
"""A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. """

num = int(input("enter the number: "))
if num >1:
                     # If num is divisible by any number between 2 and num / 2, it is not prime.

    for i in range(2,int(num/2)+1):
        if (num % i) ==0:
            print(num, "is not a prime number")
            break
    else:
            print(num, "is prime number")

# else:
#     print(num, "is not a prime number")

"""enter the number: 35
35 is not a prime number"""


# print all Prime numbers in an Interval

# num1 = 20
# num2 = 50
# for i in range(num1, num2+1):
#     if i>1:
#         for j in range(2,i):
#             if( i % j==0):
#                 break
#         else:
#             print(i)

"""
23
29
31
37
41
43
47"""


