#  Object-Oriented Programming (OOP) in Python
# OOP focuses on creating reusable code by organizing it around objects and classes. Below are the core concepts illustrated in your slides.




# 🧩 1. Classes and Objects
# Class: A blueprint for creating objects, containing attributes and methods.
# Object: An instance of a class with actual values.
# Example: Defining a Class and Creating an Object

class Student:
    roll = ""   # Attribute 1
    gpa = ""    # Attribute 2

# Creating an object
kamal = Student()
kamal.roll = 10
kamal.gpa = 3.75
print(f"Roll = {kamal.roll}, GPA = {kamal.gpa}")
# Output:
# Roll = 10, GPA = 3.75



# 🧩 2. Methods in Python
# A method is a function defined inside a class that operates on its objects.
# Example: Method Implementation

class Student:
    def set_value(self, a, b):
        self.roll = a
        self.gpa = b

    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")

# Creating an object and calling methods
kamal = Student()
kamal.set_value(10, 3.75)
kamal.display()
# Output:
# Roll = 10, GPA = 3.75



# 🧩 3. Constructors: Default & Parameterized
# Constructor is a special method (__init__) called when an object is created.
# 3.1 Default Constructor

#  __init__ is a constractor. we use constractor when we want to initialze any value in a object
class Student:              
    def __init__(self):
        self.section = "A"

    def display(self):
        print(f"Section = {self.section}")

# Creating object
kamal = Student()
kamal.display()
# Output:
# Section = A



# 3.2 Parameterized Constructor
class Student:
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll = {self.roll}, GPA = {self.gpa}")

# Creating object with parameters
kamal = Student(10, 3.75)
kamal.display()
# Output:
# Roll = 10, GPA = 3.75





# 🧩 4. Inheritance
# Inheritance allows a child class to inherit properties and methods from a parent class.

# 4.1 Single Inheritance
class A:
    def display1(self):
        print("This is class A")

class B(A):
    def display2(self):
        print("This is class B")

obj = B()
obj.display1()
obj.display2()
# Output:
# This is class A
# This is class B





# 4.2 Multiple Inheritance
class A:
    def display1(self):
        print("This is class A")

class B:
    def display2(self):
        print("This is class B")

class C(A, B):
    def display3(self):
        print("This is class C")

obj = C()
obj.display1()
obj.display2()
obj.display3()
# Output:
# This is class A
# This is class B
# This is class C


# 🧩 4.3. Hierarchical Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

obj1 = Child1()
obj2 = Child2()

obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
# Output:
# This function is in parent class.
# This function is in child 1.
# This function is in parent class.
# This function is in child 2.





# 🧩 4.4. Multilevel Inheritance
class A:
    def display1(self):
        print("This is class A")

class B(A):
    def display2(self):
        print("This is class B")

class C(B):
    def display3(self):
        print("This is class C")

obj = C()
obj.display1()
obj.display2()
obj.display3()
# Output:
# This is class A
# This is class B
# This is class C



# 🧩 5. Encapsulation
# Encapsulation refers to bundling data and methods within a single unit (class).
class Student:
    def __init__(self, name, roll):
        self.__name = name  # Private attribute
        self.roll = roll

    def get_name(self):
        return self.__name

# Accessing encapsulated data
kamal = Student("Kamal", 10)
print(kamal.get_name())  # Output: Kamal
print(kamal.roll)        # Output: 10






# 🧩 6. Polymorphism
# Polymorphism means using the same function name for different types or functionalities.
# Built-in Polymorphic Function

print(len("Aksadur"))   # Output: 7
print(len([10, 20, 30]))  # Output: 3
# User-defined Polymorphic Function
#  here z=0 -->> refer if any 3rd argument send it will work ok! if does not come there will be no problem!! **** exciting solution ***
def add(x, y, z=0):
    return x + y + z

print(add(30, 20))      # Output: 50
print(add(10, 30, 20))  # Output: 60





# 🧩 7. Method Overloading & Overriding
# Method Overloading (Same method name, different parameters):
# Python doesn’t support method overloading directly. However, you can achieve a similar effect using default parameters.

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9


# Method Overriding (Child class overrides parent class method):
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        print("This is child class")

obj = Child()
obj.show()  # Output: This is child class



# 🧩 8. Pass Statement
# pass is a placeholder used when you need to write code later.
class Person:
    pass  # Will implement later

def my_function():
    pass  # Will add logic later

# continue....
