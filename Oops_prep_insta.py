#  OOPs Concept in Python


# Class
# class Prepster: 
#     def __init__(self, name , userid,password):
#         self.name=name 
#         self.userid=userid 
#         self.password=password


# Objects

"""
class Prepster: 
    def __init__(self, name , userid, password):
        self.name= name 
        self.userid= userid 
        self.password= password
 
obj1=Prepster("Sourav", "vk18", "722139") ##object 
print(obj1.name)

"""


#method

"""
class Prepster: 
    def __init__(self, name , userid, password):
        self.name= name 
        self.userid= userid 
        self.password= password
    
    def display(self): ##method of an class 
        print(self.name)
        print(self.userid)
 
obj1=Prepster("Sourav", "vk18", "722139") ##object 
obj1.display()

"""

#Inheritance

# li=[1,2,3,4]
# def add(lis):
#     s=0
#     for i in lis:
#         s+=i 
#     return s 
    
# print('First method : ',add(li))
# print('2nd Method:',sum(li))


#  (init with inheritance):

"""
class PrepInsta:
    def __init__(self,name):
        self.name=name 
        print('You are in Parent class')
class Prepster(PrepInsta): 
    def __init__(self, name): ##constructor 

        PrepInsta.__init__(self,name) 
        print('You are in Child Class')
        self.name=name  ## assigning values to variables

ob1=Prepster('Sourav') ##object


#output- 
# You are in Parent class
# You are in Child Class
"""



"""

class PrepInsta:
    def __init__(self,name):
        self.name=name 
        print('You are in Parent class')
class Prepster(PrepInsta): 
    def __init__(self, name): ##constructor 

        
        print('You are in Child Class')
        self.name=name  ## assigning values to variables
        PrepInsta.__init__(self,name) 

ob1=Prepster('Sourav') ##object

# o/p- 
# You are in Child Class
# You are in Parent class

"""

#Import in python

# import module_name

# import collections
# D = collections.defaultdict(int)
# D[1]=10
# print(D[1])


# from module_name import class_name

# from collections import defaultdict
# D = defaultdict(int)
# D[1]=10
# print(D[1])

#  from module_name import *

# from collections import *
# D = defaultdict(int)
# D[1]=10
# print(D[1])

#  import module_name as m_n

# import collections as cs
# D = cs.defaultdict(int)
# D[1]=10
# print(D[1])


# from module_name import class as cl

# from collections import defaultdict as DD
# D = DD(int)
# D[1]=2
# print(D[1])


# Self in python

"""
class PrepInsta:
    def __init__(self,name):
        self.name=name 
        #print(‘You are in Parent class’)
    def display(self):
        print(self.name)
        print('U are in Display Function ')
ob1=PrepInsta('Sourav') ##object 
ob1.display()
"""

#  Getter and setter

"""
class A(object): 
  
    
    def __init__(self): 
        self.name = None
        self.userid=0 
    #getter
    def get_name(self):
        return (self.name)  

    #setter  
    def set_name(self,x):
        self.name=x      

ob = A()
ob.set_name('Sourav')
print(ob.get_name())

"""

#Getters and setter

"""

class A(object): 
    
    def __init__(self): 
        self._name = None
        self.userid=0 
    #getter
    def get_name(self):
        print('IN getter')
        return (self._name)  

    #setter  
    def set_name(self,x): 
        print('In setter')
        self._name=x      
    def del_name(self): 
        print('Delete')
        del self._name 
    name=property(get_name,set_name, del_name)


ob = A()
ob.name='Sourav Lakshan'
print(ob.name)

# o/p- 
# In setter
# IN getter
# Sourav Lakshan

"""

#  Encapsulation in Python

"""

#  protected members

# Creating a PrepInsta class
class PrepInsta:
    def __init__(self):
        # Protected member
        self._a = 2

# Creating a Prepster class 
class Prepster(PrepInsta):
    def __init__(self):
        
        # Calling constructor of
        # PrepInsta class
        PrepInsta.__init__(self) 
        print('Calling protected member of PrepInsta class: ')
        print(self._a)

obj1 = Prepster()
        
obj2 = PrepInsta()

# Calling protected member
# Outside class will result in 
# AttributeError

print(obj2._a)
print(obj2.a) # Attribute error


# o/p- 
# Calling protected member of PrepInsta class: 
# 2
# 2
"""


"""
#  private members

# Creating a PrepInsta class
class PrepInsta:
    def __init__(self):
        # Private member
        self.__a = 2

# Creating a Prepster class 
class Prepster(PrepInsta):
    def __init__(self):
        
        # Calling constructor of
        # PrepInsta class
        PrepInsta.__init__(self) 
        print('Calling private member of PrepInsta class: ')
        print(self.__a)

obj1 = Prepster()   #this will also raise an error.
        
obj2 = PrepInsta()

# Calling private member
# Outside class will result in 
# AttributeError

# print(obj2.__a)
print(obj2.a)  # attribute error


"""


# data Abstraction in python

"""

from abc import ABC

class llgm(ABC): #abstract classdef calculate_area(self): #abstract methodpass

    pass
class Square(llgm):

  length = 6
  def Area(self):

    return self.length * self.length 

class Circle(llgm):
  radius =5

  def Area(self):
    return 3.14 * self.radius * self.radius

sq = Square() #object created for the class ‘Square’

cir = Circle() #object created for the class ‘Circle’

print('Area of a Square:', sq.Area()) #call to ‘calculate_area’ method defined inside the class ‘Square’

print('Area of a circle:', cir.Area()) #call to ‘calculate_area’ method defined inside the class ‘Circle’.


# o/p- 
# Area of a Square: 36
# Area of a circle: 78.5

"""

# inheritance in python.

#single inheritence
"""
class PrepInsta:
    def __init__(self, a):
        self.a = a
        print(self.a)

class Prepster(PrepInsta):
    def __init__(self,a):
        PrepInsta.__init__(self,a)

obj1 = Prepster(10)
"""

#multiple inheritance
"""
class A(object):
    def __init__(self):
        self.str1 = "prepinsta"
        print("A")
class B(object):
    def __init__(self):
        self.str2 = "prepster"
        print("B")

class C(A,B):
    def __init__(self):  
        #calling constructor of A and B classes..
        A.__init__(self) 
        B.__init__(self)
        print("C")

    def printstrs(self):
        print(self.str1, self.str2)

obj = C()
obj.printstrs()

# A
# B
# C
# prepinsta prepster

"""
#multilevel inheritance.
"""
class A(object):
    def __init__(self):
        self.str1 = "prepinsta"
        print("A")
class B(object):
    def __init__(self):
        self.str2 = "prepster"
        A.__init__(self)
        print("B")

class C(A,B):
    def __init__(self):
        B.__init__(self)
        print("C")

    def printstrs(self):
        print(self.str1, self.str2)

obj = C()
obj.printstrs()

"""

# Access modifiers in python

#Public access modifier

# class A(object): 
#     def __init__(self, name , userid): 
#         self.name = name 
#         self.userid=userid 
#     def display(self):
#         print(self.name)
#         print(self.userid)
        
 

# ob = A('Sourav' , 'sourav@.com')
# print(ob.userid)  
# ob.display()


#protected access modifier
"""
class A(object): 
    _name=None 
    _userid=None
    def __init__(self, name , userid): 
        self._name = name 
        self._userid=userid 
 

    def _display(self):
        print(self._name)    
 
class B(A): 
    def __init__(self,name,userid):
        A.__init__(self,name,userid)       
ob = B('Sourav' , 'sourav@.com')
 
print(ob._userid)  
ob._display()

"""

#private access modifier

"""
class A(object): 
    #private member
    __name=None 
    __userid=None
    def __init__(self, name , userid): 
        self.__name = name 
        self.__userid=userid 
 

    def __display(self):
        print(self.__name)    
    def dis(self):
        self.__display()
class B(A): 
    def __init__(self,name,userid):
        A.__init__(self,name,userid)    

ob = B('Sourav' , 'sourav@gmail.com')
ob.dis()
# print(ob.__userid)    #if u conmment both these, it will raise an error
 
# ob.__display()

"""
#constructor in python--

# default constructor.

# class A(object): 
#     def __init__(self): 
#         self.str1 = 'Sourav'
#         print( self.str1) 
#         print('In constructor')

# ob = A() 


#parametized constructor

"""
class A(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name
ob = A('sourav', '27')
print(ob.age)
print(ob.name)
"""


# destructor in python

# class A(object): 
#     def __init__(self): 
#         self.str1 = 'PrepInsta'
#         print('Object Created' , self.str1) 
#     def __del__(self):
#         print('DEstructor is called automatically')

# ob = A() 

# Object Created PrepInsta
# DEstructor is called automatically

"""
class A(object): 
    def __init__(self): 
        self.str1 = 'PrepInsta'
        print('Object Created' , self.str1) 
    def __del__(self):
        print('DEstructor is called manually')

ob = A() 
del ob

obj1 = A

# Object Created PrepInsta
# DEstructor is called manually
"""