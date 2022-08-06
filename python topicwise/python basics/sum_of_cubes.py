
# Program for cube sum of first n natural numbers

#method 1--

# n = 5
# n= int(input("enter the number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum +(i*i*i)
# print(sum)

""" 
o/p-- 225

enter the number: 4
100
"""


# methdo 2--

# def cube_sum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i*i*i
#     print("the cube sum of",n, "is :",  sum)
# cube_sum(6)

# the cube sum of 6 is : 441


# method 3--  direct mathematical formula which is-- [ (n ( n + 1 ) / 2) ^ 2 ]


def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)
  
print(sumOfSeries(6))

# o/p- 441
