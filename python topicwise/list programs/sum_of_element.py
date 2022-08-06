# list = [10,20,30,40,50, 60, 70, 80]
# total = 0
# for i in range(0,len(list)):
#     total = total +list[i]

# print(total)



# def sum(list):
#     total =0
#     for i in range(0,len(list)):
#         total= total +list[i]
#     return total
# list =[ 100,300,500,700,900]
# print("The sum is:", sum(list))

# The sum is: 2500


#another method --


def sum(list):
    total =0
    for i in list:
        total= total +i
    return total
list =[ 100,300,500,700,900]
print("The sum is:", sum(list))