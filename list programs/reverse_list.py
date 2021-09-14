# def reverse(list):
#     list.reverse()
#     return list

# list =[10,20,30,40,50]
# print("the reverse list is:", reverse(list))

# the reverse list is:  [50, 40, 30, 20, 10]

# method -2--

def reverse(list):
    new_list= list[::-1]
    return new_list

list =[20,30,40,50,60]
print( "the reverse list is:", reverse(list))

""" the reverse list is: [60, 50, 40, 30, 20] """


