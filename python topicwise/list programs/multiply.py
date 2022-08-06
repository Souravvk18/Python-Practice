# program to find multiply of numbers in a list


# list = [1,2,3,4,5, 6, 7, 8]
 
# total =1
# for i in list:
#     total = total*i

# print("the multiply is:",total)

"""the multiply is: 40320"""



list = [1,2,3,4,5, 6, 7, 8]
def multiply(list):
    mul =1
    for i in list:
        mul=mul*i

    return mul
print(multiply(list))

"""the multiply is: 40320"""
