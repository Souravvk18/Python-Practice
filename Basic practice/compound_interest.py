# metod 1

p = 1000
t = 3
r = 10
amount = p*(pow((1+ r/100), t))
ci= amount - p
print("the compound interest is", ci)

# the compound interest is 331.00000000000045

#                                               method 2--- input given

# def compound(p,r,t):
#     amount = p*(pow((1+ r/100), t))
#     CI= amount - p
#     print("the compound interest is", CI)

# compound(1000,5,2)

#     return CI
# print(compound(1000,5,2))


# the compound interest is 102.5

#                                   user input-----

# def compound(p,r,t):
#     amount = p*(pow((1+ r/100), t))
#     CI= amount - p
#     print("the compound interest is", CI)

# p =float(input("enter the value of p:"))
# r =float(input("enter the value of r:"))
# t =float(input("enter the value of t:"))

# compound(p,r,t)
