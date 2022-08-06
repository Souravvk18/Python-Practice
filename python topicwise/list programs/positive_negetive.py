# program to print positive numbers in a list

# method 1, using for loop--

# list= [ 10, - 2, -5, 20, -10, 40, -7]

# for num in list:
#     if num>=0:
#         print(num, end=" ")

# o/p-  10 20 40


# method 2 , using while loop

# list= [ 10, - 2, -5, 20, -10, 40, -7]
# num = 0
# while (num < len(list)):
#     if list[num] >= 0:
#         print(list[num], end=" ")
    
#     num += 1

# o/p - 10 20 40 



# program to print negetive numbers in a list

# list= [ 10, - 2, -5, 20, -10, 40, -7]

# for num in list:
#     if num<0:
#         print(num, end=" ")

"o/p- -2 -5 -10 -7 "


# method 2 , using while loop

list= [ 10, - 2, -5, 20, -10, 40, -7, 50, 60]
num = 0
while (num < len(list)):
    if list[num] < 0:
        print(list[num], end=" ")
    
    num += 1

# 0/p- -2 -5 -10 -7 