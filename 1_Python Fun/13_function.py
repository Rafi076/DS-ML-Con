
# Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Output: Hello, Guest!
greet("Alice")    # Output: Hello, Alice!
print('/')



# Keyword Arguments -->> You can pass arguments using key = value syntax, allowing you to change their order.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Alice")  # Output: My name is Alice and I am 25 years old.
print('/')

#  another
def my_function(child1, child2, child3):
    print("The youngest child is", child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")



# Default Parameter Value
# You can define a default value for a parameter, which will be used if no argument is passed.

# Example: Default Parameter Value
def my_function(country="Norway"):
    print("I am from", country)

my_function("Sweden")  # Output: I am from Sweden
my_function()          # Output: I am from Norway
my_function("Brazil")  # Output: I am from Brazil



# Key Value
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  
# Output: 
# name: Alice
# age: 25
print('/')





#  Lambda Functions (Anonymous Functions) --> A lambda function is a small anonymous function with no name.A lambda function is a small anonymous function with a single expression.
# Syntax:---->>  lambda arguments: expression
square = lambda x: x * x
print(square(6))  # Output: 36
print('/')


# Example
def apply_operation(operation, x, y):
    return operation(x, y)

add = lambda a, b: a + b
print(apply_operation(add, 5, 3))  # Output: 8
print('/')

# another
# Simple lambda function
x = lambda a: a + 10
print(x(5))  # Output: 15

# Lambda function with multiple arguments
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # Output: 13

# Lambda function for cubing a number
lambda_cube = lambda y: y * y * y
print(lambda_cube(5))  # Output: 125




# Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
print('/')





# Docstrings for Functions ---->> A docstring is a string literal used to document what the function does.
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print(multiply.__doc__)  # Output: This function multiplies two numbers.
print('/')

# Docstrings
# A docstring provides documentation for a function and can be accessed via .__doc__.

# Example: Using a Docstring
def Add(a, b):
    '''This function adds two numbers and returns the result.'''
    return a + b

print(Add(10, 20))        # Output: 30
print(Add.__doc__)  # Output: This function adds two numbers and returns the result.






# Functions with Side Effects --->> A side effect is when a function affects some state outside its scope.
my_list = [1, 2, 3]

def modify_list(lst):
    lst.append(4)

modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
print('/')






# Decorators (Function Modifiers) --->> A decorator adds extra functionality to a function without modifying its structure.
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
print('/')




# Generator Functions --->> A generator function uses yield to return a sequence of values lazily, instead of returning them all at once.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(3):
    print(number)

# Output:
# 1
# 2
# 3
print('/')






#  Nested Functions (Functions within Functions) --->> A nested function is a function defined inside another function.
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from inner function!")
# Output: Hello from inner function!
print('/')





# Handling Errors in Functions ---->> You can handle exceptions using try-except inside functions.
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero
print('/')





#  Asynchronous Functions (async / await) --->> You can define asynchronous functions to improve concurrency using async and await.
import asyncio

async def greet():
    print("Hello!")
    await asyncio.sleep(1)
    print("Goodbye!")

asyncio.run(greet())
# Output:
# Hello!
# Goodbye! (after 1 second)
print('/')





# Built-in Functions
# Python provides many built-in functions to perform common tasks.

# Examples: Built-in Functions-->> Using the 'print' function
print("Hello World")  # Output: Hello World

# Finding the length of a list
mylist = ["apple", "banana", "cherry"]
x = len(mylist)
print(x)  # Output: 3

# Getting input from the user
x = input('Enter your name: ')
print('Hello, ' + x)





# Map and Filter Functions
# map(): Applies a function to all elements in an iterable.
# filter(): Filters elements based on a function's result.
# Example: Using map()
def myfunc(a):
    return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))  # Output: [5, 6, 6]

# Example: map() with Squaring Numbers
def square(x):
    return x * x

num = [1, 2, 3, 4, 5]
result = list(map(square, num))
print(result)  # Output: [1, 4, 9, 16, 25]

# Example: Using filter()
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    return x >= 18

adults = list(filter(myFunc, ages))
print(adults)  # Output: [18, 24, 32]

# Example: filter() with Lambda Function
num = [5, 12, 17, 18, 25, 32]
result = list(filter(lambda x: x % 2 == 0, num))
print(result)  # Output: [12, 18, 32]