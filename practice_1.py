# 1. Check whether a specified value is contained in a group of values

def group(data, n):
    for value in data:
        if n==value:
          return True
    return False

# print(group([2,3,4,5,6], 5))
# print(group([2,3,4,5,6], 10))

"""
True
False
"""


def num(data, n):
    for i in data:
        if n == i:
            return True
    return False

# print(num([2,3,4,5,6], 8))


# 2. Create a histogram from a given list of integers

# def histogram(items):
#     for n in items:
#         output=""
#         times= n
#         while (times> 0):
#             output += "*"
#             times = times-1
#         print(output)

# histogram([2,4,5,3])
# histogram([7,6,5,4])

"""
**
****
*****
***


*******
******
*****
****
"""
# def  histogram(items):
#     for n in items:
#         output = ""
#         times = n
#         while (times > 0):
#             output += "*"
#             times = times -1
#         print(output)

# histogram([3,4,5,6])



# 3. Concatenate all elements in a list into a string and return it
def concatenate(list):
    result = ""
    for i in list:
        result += str(i)
    return result
# print(concatenate([2,3,5,6,7]))
# print(concatenate([2,32,45,67]))
# print(concatenate(["hello", ' sourav', ' cse', ' engineer']))


"""
23567
2324567
hello sourav cse engineer
"""

# 4. Print all even numbers from a given numbers list in the same order and
#  stop the printing if any numbers that come after 237 in the sequence.

numbers = [ 815, 67, 104, 58, 512, 24, 892, 894, 843, 831, 445, 42, 717, 958,743, 527]
# for x in numbers:
#     if x==42:
#         print(x)
#         break
#     # elif x % 2 != 0:
#     #     print(x)
#     elif x % 2 == 0:
#         print(x)
    

"""
815
67
843
831
445
42


104
58
512
24
892
894
42
"""

# list = [ 20, 25, 30, 35,40, 42, 45, 50]
# for i in list:
#     if i == 42:
#         print(i)
#         break
#     elif i % 2 ==0:
#         print(i)
        

# 5. Print out a set containing all the colors from a list which are not present in other list.

list_1 = set(["White", "Black", "Red", "orange"])
list_2 = set(["Red", "Green", "purple"])
# print("difference of list_1 and List_2:", list_1.difference(list_2))
# print( "difference of list_2 and List_1:", list_2.difference(list_1))

"""
difference of list_1 and List_2: {'White', 'orange', 'Black'}
difference of list_2 and List_1: {'purple', 'Green'}
"""

# 6. Accept the base and height of a triangle and compute the area
# base=int(input("Enter the base value:"))
# height=int(input("Enter the height value:"))

# area = (base*height)/2
# print("the area is :", area)

"""Enter the base value:10
Enter the height value:5
the area is : 25.0

Enter the base value:30
Enter the height value:20
the area is : 300.0
"""

# 7. Compute the greatest common divisor (GCD) of two positive integers

def gcd(x,y):
    gcd = 1 
    if x % y ==0:
        return y
    for k in range(int(y/2), 0 , -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd
# print(gcd(10,25))
# print(gcd(42,12))

# print(gcd(4,10))
# print(gcd(40,8))
"""
5
6

2
8
"""

# 8.  Get the least common multiple (LCM) of two positive integers
def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
# print(lcm(4, 6))
# print(lcm(35, 10))
# print(lcm(60, 100))

"""
12
70 
300

"""
# 9. Sum of three given integers. However, if two values are equal sum will be zero

def sum(x,y,z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z
    return sum

# print(sum(10,20,30))
# print(sum(10,20,20))
# print(sum(500,200,300))

"""
60
0
1000
"""
# 10. Sum of two given integers. However, if the sum is between 15 to 20 it will return 20
def sum(x,y):
    sum = x + y
    if sum in range(15,20):
        return 20
    else:
        return sum

# print("sum of two numbers is :", sum(20,30))

# print("sum of two numbers is :", sum(10,8))

"""
sum of two numbers is : 50
sum of two numbers is : 20
"""

# 11. Return true if the two given integer values are equal or their sum or difference is 5
def number(x,y):
    if x == y or (x-y) == 5 or (x + y) == 5:
        return True
    else:
        return False

# print(number(9,4))
# print(number(2,3))
# print(number(9, 5))

"""
True
True
False
"""

# 12. Add two objects if both objects are an integer type

def number(a,b):
    if not (isinstance(a,int) and isinstance(b, int)):
        return "number must be integers !"
    return a+b

# print(number(20,30))
# print(number(10, 5.42))
# print(number('hello', 10))

"""50
number must be integers !
number must be integers !"""


list1 =['hello', 'hii', 'byy']
# list2= [ 'hihi', 'hehe']
list2= ['200', '300']

list3 = list1+list2
# print(list3)

"""
['hello', 'hii', 'byy', 'hihi', 'hehe']
['hello', 'hii', 'byy', '200', '300']
"""

# 13. Display your details like name, age, address in three different lines
def details():
    name, age = "sourav", 22
    address = "bankura, west bengal, india"
#     print("Name: {} \n Age: {} \n Address: {}".format(name, age, address))

# details()

"""
Name: sourav 
 Age: 22
 Address: bankura, west bengal, india
 """

# 14. Python program to solve (x + y) * (x + y)

x, y= 4, 5
result = x*x + 2*x*y + y*y
# print("({} + {})^2 = {} ".format(x, y,result))

""" (4 + 5)^2 = 81 """

# 15. Parse a string to Float or Integer

n = "246.2458"
# print(float(n))
# print(int(float(n)))

"""
246.2458
246
"""
