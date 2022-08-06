# program to interchange first and last elements in a list

# def swap(list):
#     list[0], list[-1] = list[-1], list[0]
#     print("the swap list is: ",list)

# # list =[ 20,5,10,15]

# list =[ 100, 20,5,10,15, 40, 50]
# swap(list)


"""
the swap list is:  [15, 5, 10, 20]
the swap list is:  [50, 20, 5, 10, 15, 40, 100]
"""

def swap(list):
    # size=len(list)
    temp=list[0]
    list[0] = list[-1]
    list[-1] = temp
    return list
list=[10,20,30,40,50]
print(swap(list))

"""[50, 20, 30, 40, 10]"""