
# print(2/1)
# print(1/0)
# ZeroDivisionError: division by zero
'''
            Except Handling :- Exception are errors detected at the time of program execution.       
'''

# print("abc"+2)
# o/p- only concatenate str (not "int") to str

# x= input("Enter Number1:")
# y= input("Enter Number2:")
# z=int(x)/int(y)
# print("Division is:",z)

'''
output:
Enter Number1:70
Enter Number2:5
Division is: 14.0

number1:4
number2:2   o/p- 2 , it will run.

number1:3
number2:0
it will show you errer (ZeroDivisionError: division by zero)
'''


# x= input("Enter Number1:")
# y= input("Enter Number2:")
# try:
#     z=int(x)/int(y)
# except Exception as e:
#     print('exception occured:',e)
# # except ZeroDivisionError as e:
# #     print('Division by zero exception')
#     z=None
# print("Division is:",z)

'''
Enter Number1:50
Enter Number2:0
Division by zero exception
Division is: None

output:
number1:4
number2:2   o/p- 2 

number1:3
number2:0 , Noe error.
o/p- exception occured / division by zero exception , division is none. it does not show you any error.

"google "Python builtin exception" to see list of standard exceptions in python.

'''

# x= input("Enter Number1:")
# y= input("Enter Number2:")
# try:
#     z= x/int(y)
# except TypeError as e:
#     print('type error exception')
# #  except Exception as e:
# #     print('exception type:',type(e).__name__)
#     z=None
# print("Division is:",z)
'''
Enter Number1:10
Enter Number2:7
type error exception
Division is: None

number1:4
number2:3
o/p- type error exception, but no runtime error
Division is: None
'''





                        # CLASS
''' it is important to do programming using object oriented programming using class & objects.
'''
# class Human:
#     def __init__(self,name,occupation):
#         self.name=name
#         self.occupation= occupation
#
#     def do_work(self):
#         if self.occupation=="Cricket player":
#             print(self.name,"plays Cricket")
#         elif self.occupation== "actor":
#             print(self.name,"shoot a film")
#         elif self.occupation=="Politician":
#             print(self.name,"Best Prime Minister ever of India")
#
#     def speaks(self):
#         print(self.name,"Says How are You?")
#
# sushant=Human("Sushant singh",'actor')
# sushant.do_work()
# sushant.speaks()
# #
# virat=Human("Virat Kohli",'Cricket player')
# virat.do_work()
# virat.speaks()
#
# modi=Human("Narendra Modi", 'Politician')
# modi.do_work()
# modi.speaks()

'''
output-
Sushant singh shoot a film
Sushant singh Says How are You?
Virat Kohli plays Cricket
Virat Kohli Says How are You?
Narendra Modi Best Prime Minister ever of India
Narendra Modi Says How are You?

'''



'''
                                Inheritance
benefits of inheritancee: 1- code reduce, 2- extensibility, 3- readability.

'''
# class vehicle:
#     def general_usage(self):
#         print("general usage:Transportation")
# class car(vehicle):
#     def __init__(self):
#         print("i am car")
#         self.wheels=4
#         self.roofs=True
#
#     def specific_usage(self):
#         self.general_usage()
#         print("specific use: mainly for work purpose and vacation with family.")
#
# class motorcycle(vehicle):
#         def __init__(self):
#             print("i am motorcycle")
#             self.wheels = 2
#             self.roofs = False
#
#         def specific_usage(self):
#             self.general_usage()
#             print("specific use: for Road trip and racing.")
#
# c= car()
# c.specific_usage()
#
# m= motorcycle()
# m.specific_usage()
#
# print(isinstance(c,car))
# print(isinstance(c,motorcycle))
#
# print(issubclass(car,vehicle))
# print(issubclass(car,motorcycle))

'''
output-
i am car
general usage:Transportation
specific use: mainly for work purpose and vacation with family
i am motorcycle
general usage:Transportation
specific use: for Road trip and racing.

True
False
True
False

'''


#           Multiple Inheritance


# class father():
#     def gardening(self):
#         print("I enjoy Gardening")
#
# class mother():
#     def cooking(self):
#         print("i Love cooking")
#
# class child(father,mother):
#     def sports(self):
#         print("i enjoy sports")

# c=child()
# c.gardening()
# c.cooking()
# c.sports()

''''
output-
I enjoy Gardening
i Love cooking
i enjoy sports
'''

class father():
    def skills(self):
        print("teaching & programming")

# class mother():
#     def skills(self):
#         print("cooking & art")
#
# class child(father,mother):
#     def skills(self):
#         father.skills(self)
#         mother.skills(self)
#         print("sports & Singing")
#
# c= child()
# c.skills()

'''
output-
teaching & programming
cooking & art
sports & Singing

'''

# Raise exception

# try:
#     raise MemoryError('memory error')
# except MemoryError as e:
#     print(e)

# # output- memory error


# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#
#     def print_exception(self):
#         print("user defined exception:",self.msg)
# try:
#     raise Accident("crash between two cars")
# except Accident as e:
#     e.print_exception()

# output- user defined exception: crash between two cars



# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def handle(self):
#         print("accident occured. take detour")
#
#     def print_exception(self):
#         print("user defined exception:",self.msg)
# try:
#     raise Accident("crash between two cars")
# except Accident as e:
#     # e.print_exception()
#     e.handle()

# output- accident occured. take detour.


                # Finally statement







                    # Iterator

# a=["hey","bro","you'r","awesome"]
# for i in a:
#       print(i)
# itr=iter(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

'''
output-
hey
bro
you'r
awesome
'''

# itr=reversed(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

'''
output-
awesome
you'r
bro
hey

'''


                # Example of Iterator
                # iterator through list

# for element in [1,2,3]:
#     print(element)

''' o/p- 1
2
3
'''

                # iterator through tuple

# for element in (5,10,15):
#     print(element)

'''o/p- 5
10
15

'''
                # iterator through doct

# for key in {'one':1,'two':2,'three':10}:
#     print(key)

'''o/p- one
two
three
'''

                # iterator through string(char)

# for char in "123":
#     print(char)

'''o/p- 1
2
3
'''

            # iterating through everyline in a file
# for line in open("C\\Downloads\\funny.txt"):
#     print(line,end='')


'''
implement remote control class, that allow you to press'next' button to go next channel.
'''

# class RemoteControl():
#     def __init__(self):
#         self.channels=["opindia","india tv","republic","abp news", "pogo","discovery","cnn","india today","aaj tak"]
#         self.index= -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index==len(self.channels):
#             raise StopIteration
#
#         return self.channels[self.index]
#
# r=RemoteControl()
# itr=iter(r)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

'''
o/p- opindia
india tv
republic
abp news
pogo
'''


            # Generator- it is a simple way of creating iterator

# def remote_control_next():
#     yield"cnn"
#     yield"cspn"
#
# itr=remote_control_next()
# itr
# print(next(itr))
# print(next(itr))

# o/p- cnn, cspn

# Produce fibonacci sequence using generator

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b, a+b
# for f in fib():
#     if f>50:
#         break
#
#     print(f)

'''

output- 0 1 1 2 3 5 8 13 21 34
1- you dont need to define iter() and next() method
2-myou dont need to raise stopiteration exception

'''

# List comprehension-  it provides a way to transform one list into another.

# number= [1,2,3,4,5,6,7,8,9,10]
# even=[]
# for i in number:
#     if i%2==0:
#         even.append(i)
# print(even)

# o/p- [2, 4, 6, 8, 10]
#        or you can write the below one line code.

# even=[i for i in number if i%2==0]
# print(even)
# o/p- [2, 4, 6, 8, 10]

#                    print square

# sqr_numbers=[i*i for i in number]
# print(sqr_numbers)

# output- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# s=set([1,2,3,4,5,2,3,1])
# print(s)
# o/p- {1, 2, 3, 4, 5}

# even={i for i in number if i%2==0}
# print(even)
# o/p- {2, 4, 6, 8, 10}

#output- {2, 4, 6, 8, 10}

# cities=["mumbai", "new york", "peris"]
# countries= [ "India", "USA", "France"]
# z=zip(cities,countries)
# for a in z:
#     print(a)

'''
outcut-
('mumbai', 'India')
('new york', 'USA')
('peris', 'France')
'''

# basket={"orange","apple", "mango", "apple", "orange"}
# print(type(basket))
# print(basket)
'''
output- 
<class 'set'>
{'apple', 'orange', 'mango'}
'''

# a={}
# print(type(a))
# output- <class 'dict'>

# a=set()
# a.add(100)
# a.add(200)
# a.add(500)
# print(a)

# output- {200, 100, 500}

# a={'something'}
# print(type(a))
# o/p- <class 'set'>
'''
List allow index operation,  set doesnot allow it.
list allow duplicate operation, set does not allow it.

'''

# numbers=[1,2,3,4,6,7,3,2,1]
# unique_numbers=set(numbers)
# print(unique_numbers)
# o/p- {1, 2, 3, 4, 6, 7}

# unique_numbers.add(20)
# print(unique_numbers)
# o/p- {1, 2, 3, 4, 6, 7, 20}

#  Frozen set- it does not allow any changes

# numbers=[1,2,3,4,6,7,3,2,1]
# fs=frozenset(numbers)
# print(fs)
# o/p- frozenset({1, 2, 3, 4, 6, 7})

# frozenset({1, 2, 3, 4, 6, 7})
# fs.add(10)
# print(fs)
# AttributeError: 'frozenset' object has no attribute 'add'

#           Union, intercection, subset

# x={"a","b",'c'}
# for i in x:
#     print(i)
# y={"a","g","h"}
# print(x|y)

'''
b
c
a
o/p- union output- {'a', 'c', 'b', 'h', 'g'}
'''

# print(x&y)
# # output-intersection -{'a'}

# x={"h","g"}
# print(x<y)
# # output- True,x is a subset of y

#  Command line argument:-

# import argparse
# if __name__=="__main__":
#     parser=argparse.ArgumentParser()
#     parser.add_argument("number1",help="first number")
#     parser.add_argument("number2", help="second number")
#     parser.add_argument("operation", help="operation")
#
#     args=parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)
#     n1=int(args.number1)
#     n2 =int(args.number2)
#     result=None
#
#     if args.operation=="add":
#         result=n1+n2
#     elif args.operation=="substract":
#         result=n1-n2
#     elif args.operation=="multiply":
#         result=n1*n2
#     elif args.operation=="division":
#         result=n1/n2
#     print("result:",result)

'''
run in terminal-- 
$ python intermediate.py 3 4 add

output-3
4
add
result: 7

$ python intermediate.py 10 6 substract

10
6
substract
result: 4

>python intermediate.py 100 50 add
100
50
add
result: 150

'''



