#using chain() + loop

from itertools import chain
#getting product
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res

#iterating values
list1 =[[2,4,5], [6,7], [4,8]]

res = prod(list(chain(*list1)))

# print(str(res))
print("the total element product in list is :", res)

# the total element product in list is : 53760

