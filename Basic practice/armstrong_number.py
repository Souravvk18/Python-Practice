
# for 3 digit number.

# num = int(input("Enter the number:"))
# sum= 0
# temp = num

# while temp>0:
#     digit = temp % 10
#     sum += digit**3
#     temp //= 10

# if num ==sum:
#     print(num,"is a armstrong number")
# else:
#     print(num, "is not a armstrong number")

"""Enter the number:160
160 is not a armstrong number

Enter the number:153
153 is a armstrong number
"""

# Python Program to Find Armstrong Number between an Interval

lower =int(input("enter the lower : "))
upper = int(input("enter the upper : "))

for num in range(lower, upper+1):
    sum = 0
    temp = num
    while temp> 0:
        digit = temp % 10
        sum = sum + digit**3
        temp = temp// 10
        
        if num==sum:
            print(num)

"""
125
153
216
370
371
407
"""