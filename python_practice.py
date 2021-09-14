# 1. Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

"""Current date and time : 
2021-09-01 19:33:35
"""

# 2. Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi
# r = float(input ("Enter the radius: "))
# print ("The area of the circle is: " + str(pi * r**2))

"""
Enter the radius: 1.3
The area of the circle is: 5.3092915845667505
"""

# 3. Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
# fname = input("Enter your First Name : ")
# lname = input("Enter your Last Name : ")
# print ("Hello  " + lname + " " + fname)

"""Enter your First Name : sourav
Enter your Last Name : lakshan
Hello  lakshan sourav
"""

# 4. """Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers."""
# values = input("Enter some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

"""List :  ['3', '7', '4', '2', '1', '8']
Tuple :  ('3', '7', '4', '2', '1', '8')"""

# 5. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
# print("first color:",color_list[0], "and last color:", color_list[3])

"""first color: Red and last color: Black"""

# 6. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# a = int(input("Enter an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

""" 
Enter an integer : 7
861

Enter an integer : 5
615
"""

# 7. Write a Python program to print the calendar of a given month and year.
import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

"""
Input the year : 2021
Input the month : 8
    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
"""

# 8. Calculate number of days between two dates
from datetime import date
f_date = date(2018, 8, 1)
l_date = date(2021, 9, 1)
delta = l_date - f_date
# print("Number of days is:", delta.days)

"""Number of days is: 1127"""

# """ 9. Get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference"""

# def difference(n):
#     if n<=17:
#         return 17-n
#     else:
#        return (n-17) *2

# print(difference(25))
# print(difference(10))
# print(difference(20))
# print(difference(5))

"""
16
7
6
12
"""
# 10. Write a Python program to test whether a number is within 100 of 1000 or 2000

# def number(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(number(1000))
# print(number(900))
# print(number(1050))
# print(number(2070))

"""
True
True
True
True
"""
# 11. Calculate the sum of three given numbers, if the values are equal then return thrice of their sum

def sum_three(x,y,z):
    sum = x+y+z

    if x==y==z:
        sum=sum*3
    return sum

# print(sum_three(20,30,10))
# print(sum_three(20,20,10))
# print(sum_three(20,20,20))

"""60
50
180"""

# 12. Find whether a given number is even or odd, print out an appropriate message to the user

# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

"""Enter a number: 21
This is an odd number.

Enter a number: 10
This is an even number.
"""

# 13 Get a string which is n (non-negative integer) copies of a given string

def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

# print(larger_string('nisha + ', 5))
# print(larger_string('manu + ', 3))

"""nisha + nisha + nisha + nisha + nisha + 
manu + manu + manu +"""

# 14. Count the number 4 in a given list
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

# print(list_count_4([1, 4, 6, 7, 4, 4, 4, 4, 4]))
# print(list_count_4([1, 4, 6, 4, 7, 32]))

"""
6
2
"""

# 15. Test whether a passed letter is a vowel or not

def vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(vowel('c'))
print(vowel('e'))

"""
False
True

"""