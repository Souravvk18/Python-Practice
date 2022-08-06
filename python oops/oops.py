# Objects oriented programming. ( Youtube video )

# x = 1
# print(type(x))

# def hello():
#     print("hello")
# print(type(hello))


# Error

# x = 1
# y = "hello"
# print(x+y)  # int and string cant be added.


# x = "1"
# y = "hello"
# print(x + y)

# string = 'hello'
# print(string.upper())


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # print(name)
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age

# def bark(self):
#     print("bark")

# def add(self, x):
#     return x + 1
#
# def mul(self, x):
#     return x * 5


# d = Dog("Virat Kohli", 32)
#
# print("His Name is :", d.get_name())
#
# d.set_age(30)
# print("His age is :", d.get_age())
#
#
# d2 = Dog("Its Sourav", 25)
# print(d2.name)
# print(d2.age)

# d.bark()
# d.add(5)
# print(d.add(10))
# print(d.mul(10))
# print(type(d))


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_students(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#
#             return True
#         return False
#
#
#     def get_average(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
#
# s1 = Student("Sourav", 19, 90)
# s2 = Student("Sachin", 20, 80)
# s3 = Student("Suman", 18, 75)
# s4 = Student("Akash", 19, 70)
# s5 = Student("rajib", 20, 65)
# s6 = Student("hara", 21, 60)
#
# course = Course('science', 10)
# course.add_students(s1)
# course.add_students(s2)
# course.add_students(s3)
# course.add_students(s4)
# course.add_students(s5)
# course.add_students(s6)
#
# print("Average grade is :", course.get_average())


# print(course.students)
# print(course.students[0].name)
# print(course.students[1].age)
# print(course.students[2].grade)


# Inheritance

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#
#     def speak(self):
#         print("I dont know what to say")
#
# class Cat(Pet):
#     def speak(self):
#         print("Meow")
#
# class Dog(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old & my color is {self.color}")
#
#     def speak(self):
#         print("Bark")
#
#
# p = Pet('bhalu', 15)
# p.show()
# p.speak()
#
# c = Cat('Billi', 20)
# c.show()
# c.speak()
#
# d = Dog("doggy", 10, 'yellow')
# d.show()
# d.speak()


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#
#     def speak(self):
#         print("I dont know what to say")
#
# class Cat(Pet):
#     def speak(self):
#         print("Meow")
#
# class Dog(Pet):
#     def speak(self):
#         print("Bark")
#
#
# p = Pet('bhalu', 15)
# p.show()
# c = Cat('Billi', 20)
# c.show()
# d = Dog("doggy", 10)
# d.show()


# class Person:
#     number_of_people = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
#
#     @classmethod
#     def number_of_people_(cls):
#         return cls.number_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
#
#
# p1 = Person("hello")
# p2 = Person("sunny")
# print(Person.number_of_people_())


class Math:

    @staticmethod
    def add(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")

print(Math.add(10))

Math.pr()