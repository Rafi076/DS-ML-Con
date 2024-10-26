
# Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Output: Hello, Guest!
greet("Alice")    # Output: Hello, Alice!
print('/')



# Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Alice")  # Output: My name is Alice and I am 25 years old.
print('/')


# Key Value
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)  
# Output: 
# name: Alice
# age: 25
print('/')





#  Lambda Functions (Anonymous Functions) --> A lambda function is a small anonymous function with no name.
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

