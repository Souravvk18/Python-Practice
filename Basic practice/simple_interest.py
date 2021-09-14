# method 1

p = 1000
t = 3
r = 10

si= (p*t*r)/100
# print("simple interest is:", si)
# print("total amount is", si+p)

"""
 simple interest is: 300.0
 total amount is 1300.0
"""

#                       user input

# p =float(input(" value of p:"))
# r =float(input(" value of r:"))
# t =float(input(" value of t:"))
# si= (p*t*r)/100
# print("simple interest is:", si)

"""value of p:1000
 value of r:8.5
 value of t:2
simple interest is: 170.0"""



#                                   method 2

# def interest(p,t,r):
#     si = (p*t*r)/100
#     return si
# print(interest(1000,5,10))

# 500.0



def interest(p,t,r):
    si = (p*t*r)/100
    print("the simple interest is", si)
interest(1000, 2, 5)

# the simple interest is 100.0