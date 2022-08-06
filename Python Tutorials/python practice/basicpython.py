                                # Basic tutorial

# print("hello world")
# output- hello world

# LIST

item1="paneer"
item2="chicken"
item3="eggs"
# items=["bread","butter","meat","pasta","cake"]

# to know type of variable

# print(type(items))
# output- <class 'list'>

# # to print the list

# print(items)
# O/P- 'bread', 'butter', 'meat', 'pasta', 'cake']
# p= items[1]

# print(item3)
# o/p- eggs

# to print any particular items
# print(items[1])
# O/P- butter

 #                       # To replace any items

# items[0]="Milk"
# items[1]="banana"
# print(items)

# O/P- ['Milk', 'banana', 'meat', 'pasta', 'cake']

                       # to print multiple items

# a=items[0:2]
# print(a)
# O/P- ['bread', 'butter']

# print(items[0:3])
# o/p- ['bread', 'butter', 'meat']

                   # To insert a items at the end

# items.append("nonveg")
# print(items)
# o/p- ['bread', 'butter', 'meat', 'pasta', 'cake', 'nonveg']

              # to remove a items from the end

# items.pop()
# print(items)
# o/p- ['bread', 'butter', 'meat', 'pasta', 'cake']

                        # to insert a items in any place

# items.insert(1,"Lichi")
# print(items)
# o/p- ['bread', 'Lichi', 'butter', 'meat', 'pasta', 'cake']

                            # to remove any item

# items.remove(items[2])
# print(items)
# # o/p- ['bread', 'Lichi', 'meat', 'pasta', 'cake']
# items.remove("cake")
# del items [1]
# print(items)
# # o/p- ['bread', 'Lichi', 'meat', 'pasta']

#                     # to remove multiple items
#
# del items [2:4]
# print(items)
# # o/p- ['bread', 'pasta', 'cake']
#
#                         # clear all the items
#
# items.clear()
# print(items)
# # o/p- []
                        # to add multiple items

# items=["bread","butter","meat","pasta","cake"]
# animals=["tiger","lion","Elephant","monkey"]
# all= (animals+items)
# print(all)
# # o/p- ['tiger', 'lion', 'Elephant', 'monkey', 'bread', 'Lichi', 'butter', 'meat', 'pasta', 'cake']
#
#                             # to know the length of items
# print(len(all))
# # o/p- 10


                                # Dictionary


'''
             it allow you to store key,values etc. its very useful

'''

# dict={"tom":100000, "jarry":10000, "harry":20000}
# print(dict)
# # o/p- {'tom': 100000, 'jarry': 10000, 'harry': 20000}
#
#                             # to print particular value
# print(dict["tom"])
# # o/p- 100000
#                             # to add new values
# dict["sourav"]=30000
# print(dict)
# # o/p- {'tom': 100000, 'jarry': 10000, 'harry': 20000, 'sourav': 30000}
#
#                             # delete any value
# del dict["sourav"]
# print(dict)
# # o/p- {'tom': 100000, 'jarry': 10000, 'harry': 20000}
#
#                                 # to print all the directory value
#
# for key in dict:
#     print("key:",key,"values",dict[key])
# '''
# o/p- key: tom values 100000
# key: jarry values 10000
# key: harry values 20000
# '''
#
#                                 # to print all the directory value
#
# for key,v in dict.items():
#     print("key:", key, "values",v)
#
# '''
# o/p- key: tom values 100000
# key: jarry values 10000
# key: harry values 20000
# '''
#
# print(dict)


#                                     #TUPLE
# tup=("hello","hii","bye")
# print(type(tup))
# print(tup)
# # o/p- <class 'tuple'>
# # ('hello', 'hii', 'bye')
#
# # tuple is unchangeable, you cant change or replace value
# # tup[0]="hey"
#
#                         # to print single or particular item
#
# a=tup[1]
# print(a)
# print(tup[2])
# # o/p- bye
#
# tup1=(10,20,30)
# print(type(tup1))
# # o/p- <class 'tuple'>
# print(tup1)
# # o/p- (10, 20, 30)
#
#                 # to add multiple items
#
# tups= tup+tup1
# print(tups)
# # o/p- ('hello', 'hii', 'bye', 10, 20, 30)


                                        # IF STATEMENT
# operators:- ==, !=, <=, >=, <,>, &&.

                                # to find a number is even or odd

# num=input("enter a number:\n ")
# num=int(num)
# if num%2==0:
#     print("number is even")
# else:
#      print("number is odd")
'''
o/p- enter a number:
 7
number is odd.

enter a number:
 4
number is even

'''



                                        # Age related problem

# age=input("Enter your Age:\n")
# age=int(age)
# if(age>18):
#     print("you can drive car")
# elif(age==18):
#     print("you r an awesome teen")
# else:
#     print("you cant drive")

'''o/p-
Enter your Age:
45
you can drive car.

Enter your Age:
10
you cant drive.
'''
                                        # Restuarent Menu

# indian=["samosa","tea","chop"]
# chinese=["egg role","chawmin","fried rice"]
# italian=["pizza","pasta","burger"]
# dish= input("Enter a dish name:\n")
# if dish in indian:
#     print("its indian dish")
# elif dish in chinese:
#     print("its chinese dish")
# elif dish in italian:
#     print("its italian dish")
# else:
#     print("Based on my knowlegde i dont know about", dish)

'''o/p-
Enter a dish name:
tea
its indian dish.

Enter a dish name:
coffee
Based on my knowlegde i dont know about coffee

'''


                                # FOR LOOPS

# exp=[200,500,1000,2000,3000]
# total=0
# for item in exp:
#     total=total+item
#     print(total)

'''o/p- 200, 700, 1700, 3700, 6700
'''
# print(total)
# o/p -- 6700

                             # print square of numbers

# for i in range(1,15):
#     print(i*i)
# # o/p- 1, 4, 9,16,25,36,49,64,81,100,121,144,169,196

# for i in range(1,10):
#     print(i*i)

                            # month number with expenses

# total=0
# exp=[2000,3000,4000,5000]
# for i in range(len(exp)):
#     print('month',(i+1),'Expense:',exp[i])
#     total=total+exp[i]

# print("total expense is:",total)
'''
month 1 Expense: 2000
month 2 Expense: 3000
month 3 Expense: 4000
month 4 Expense: 5000
total expense is: 14000


o/p- month 1 Expense: 2000
total expense is: 2000
month 2 Expense: 3000
total expense is: 5000
month 3 Expense: 4000
total expense is: 9000
month 4 Expense: 5000
total expense is: 14000
'''

                                # search for lost items


# key_location=input("Enter the locations:")
# # key_location="kitchen"
# locations=("bed room","kitchen", "dining room","chair","bathroom")
# for i in locations:
#     if i==key_location:
#         print("key is found in", i)
#         break
# else:
#     print("key is not found in", key_location)


                            # Square of numbers except even numbers

# for i in range(1,10):
#     if i%2==0:
#         continue
#     print(i*i)
# o/p- 1, 9, 25, 49, 81

                                #square of numbers in range
# i=0
# while i<=10:
#     print(i*i)
#     i=i+1

# o/p - 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 

                            #square of even numbers
# for i in range(1,10):
#     if i%2==0:
        
#       print(i*i)

# o/p- 4, 16, 36, 64



'''
    Function:- function is a block of code that performs a specific task.
    function makes your code more readable.
'''

#                     Long calculation function

def total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

january=[1000,2000,3000]
february=[500,1500,2500]
march=[100,200,500]
april=[10000,5000,3000]

sourav=total(january)
arjun=total(february)
virat= total(march)
chiku= total(april)

print("sourav's total expenses:",sourav)
print("arjun's total expenses:", arjun)
print("virat's total expenses:", virat)
print("chiku's total expenses:", chiku)

'''
o/p- sourav's total expenses: 6000
arjun's total expenses: 4500
virat's total expenses: 800
chiku's total expenses: 18000
'''

#               sum of two number using function

# def sum(a,b):
#     total=a+b
#     return total
#
# n=sum(100,200)
# print("the sum is:", n)

# o/p- the sum is: 300

# ****

# total=0
# def sum(a,b,c=40):
#     print("a:",a)
#     print("b:",b)
#     print("c:",c)
#
#     total=a+b+c
#     print("inside function:",total)
#     return total
# n = sum(10,20)
# print("outside function:",total)

'''o/p- a: 10
b: 20
c: 40
inside function: 70
outside function: 0


'''


# def sum(a,b=50):
#     print("a:",a)
#     print("b:",b)
#
#     total=a+b
#     print('sum is',total)
#     return total
# n = sum(10)
# o/p- sum is 60


'''
     json- javascript object notation
     Json is a data exchange formet similar to xml.

'''

# #        to create an Address book text file.
#
# book = {}
# book['sourav']={
#     'name':'sourav',
#     'address':'kolkata, india',
#     'phone':5657643528
# }
# book['rahul']={
#     'name':'rahul',
#     'address':'howrah, india',
#     'phone':2345678
# }
#
# import json
# s= json.dumps(book)
# with open("c://downloads//book.txt","w") as f:
#     f.write(s)
#
# '''
#         you can now read this json data using any language such as javascript,c++.
#         exchange data from python program to javascript
# '''
#
# f = open("c://downloads//book.txt", "r")
# s=f.read()
# print(s)
# # o/p- {"sourav": {"name": "sourav", "address": "kolkata, india", "phone": 5657643528}, "rahul": {"name": "rahul", "address": "howrah, india", "phone": 2345678}}
#
# print(type(s))
# # o/p- <class 'str'>

# import json
# book=json.loads(s)
# print(book)
# print(type(book))
# print(book['sourav'])


'''
                             Read and Write file 
                w- opens file for writing only.
                r- opens file for reading only.
                w+,r+  -- open file for both reading & writing.
                a- opens a file in append mode(original content will not be over written.

'''
#                           write the file

# f = open("c:\\downloads\\funny.txt",'w')
# f.write("sourav: hii, how r you")
# f.close()

#                       Read the file

# f = open("c://downloads//funny.txt","r+")
# print(f.read())
# f.close()

'''o/p- sourav: Hii, how are you?
virat: hello, i am fine. You?
sourav:  I am also fine. where are you?
virat: i am in delhi, you?
sourav: i am in Bengaluru
 Anushka: i love u guys

'''

#                   to read line by line

# f = open("c://downloads//funny.txt","r")
# for line in f:
#     print(line)
# f.close()

'''o/p- sourav: Hii, how are you?

virat: hello, i am fine. You?

sourav:  I am also fine. where are you?

virat: i am in delhi, you?

sourav: i am in Bengaluru

 Anushka: i love u guys

'''
#                   count the number of words

# f = open("c://downloads//funny.txt","r")
# for line in f:
#     token=line.split(' ')
#     print(len(token))
# f.close()
# o/p-5, 6, 8, 6, 5, 6

#           return a list (array) of worlds

# f = open("c://downloads//funny.txt","r")
# for line in f:
#     token=line.split(' ')
#     print(str(token))
# f.close()

''' o/p-
['sourav:', 'Hii,', 'how', 'are', 'you?\n']
['virat:', 'hello,', 'i', 'am', 'fine.', 'You?\n']
['sourav:', 'I', 'am', 'also', 'fine.', 'where', 'are', 'you?\n']
['virat:', 'i', 'am', 'in', 'delhi,', 'you?\n']
['sourav:', 'i', 'am', 'in', 'Bengaluru\n']
['', 'Anushka:', 'i', 'love', 'u', 'guys']

'''

#
# #             read using 'with" statement
#
# with open("c://downloads//funny.txt","r") as f:
#     print(f.read())
# print(f.closed)


