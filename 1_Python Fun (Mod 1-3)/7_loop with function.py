# Loops in Python (while loop, for loop, nested loop) - Documentation and Problem-Solving Examples


# 1. While Loop:
# The while loop in Python continues to execute a block of code as long as the condition remains True. It is useful when the number of iterations isn't fixed.

# Syntax:
# while condition:
#     # Block of code
#     # Update condition


# Example 1: Simple while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Explanation:
# The loop continues to print the value of i until i becomes greater than 5.
# After each iteration, i is incremented by 1.




# Example 2: Input until user enters 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break  # Exit the loop when user enters 0
    print(f"You entered: {num}")

# Explanation:
# The loop continues to ask for user input until 0 is entered, at which point it stops using break.






# 2. For Loop:
# A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) for a fixed number of iterations.

# Syntax:
# for item in sequence:
#     # Block of code


# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Explanation:
# The loop prints each fruit in the fruits list.


# Example 2: Using range()
for i in range(5):
    print(i)

# Explanation:
# The loop will print the numbers 0 through 4. The range(5) generates numbers from 0 to 4.






# 3. Nested Loop:
# A nested loop is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.
# Syntax:
# for outer_item in outer_sequence:
#     for inner_item in inner_sequence:
#         # Block of code


# Example 1: Multiplication table using a nested loop
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()  # Prints a newline after each inner loop
    
# Explanation:
# The outer loop iterates over numbers from 1 to 5, and for each number i, the inner loop multiplies it with numbers from 1 to 5.













# Problem-Solving Examples with Loops and Functions
# Problem 1: Taking number as input and printing it by multiplying with 2 using a function

# #         Function that multiplies the input by 2
def multiply_by_2(num):
    return num * 2

values = []
num = int(input("Enter total number of inputs: "))

for i in range(num):
    a_num = int(input("Enter a number: "))
    values.append(a_num)

for i in values:
    result = multiply_by_2(i)
    print(result, end=' ')
# Explanation:
# The function multiply_by_2 multiplies any number by 2.
# The for loop takes num inputs and stores them in the values list.
# The second for loop applies the function to each number in the list and prints the result.










# Problem 2: Calculating the average of a list of numbers
# # Function to calculate sum of numbers
def calculate_sum(store):
    total_sum = 0
    for i in store:
        total_sum += i
    return total_sum

store = []
num = int(input("Enter total number of inputs: "))

for i in range(num):
    numbers = int(input("Enter a number: "))
    store.append(numbers)

total = calculate_sum(store)
average = total / len(store)
print("Average:", average)
# Explanation:
# The function calculate_sum calculates the sum of the numbers in the store list.
# The for loop takes input from the user and adds it to the list.
# The average is calculated by dividing the total sum by the length of the list.






# Problem 3: Using while loop to keep asking for positive numbers and stopping when a negative number is entered
numbers = []
while True:
    num = int(input("Enter a positive number (negative to stop): "))
    if num < 0:
        break  # Exit the loop if the number is negative
    numbers.append(num)

print("You entered:", numbers)
# Explanation:
# The loop continues until a negative number is entered.
# Each positive number is added to the numbers list, and the final list is printed.








# Problem 4: Finding the maximum value in a list using a for loop
numbers = [10, 25, 30, 5, 20]
max_value = numbers[0]  # Assume first number is the largest

for num in numbers:
    if num > max_value:
        max_value = num

print("Maximum value:", max_value)
# Explanation:
# The for loop checks each number and updates the max_value if a larger number is found.






# Fibonacci Series:
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

# Example 1: Fibonacci Series using a for loop
# Function to print Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    print(a, b, end=' ')
    for i in range(2, n):
        c = a + b
        print(c, end=' ')
        a, b = b, c

# Get the number of terms from the user
n = int(input("Enter the number of terms: "))
fibonacci(n)







# Fibonacci Series using Recursion
# Function to find the nth Fibonacci number using recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Get the number of terms from the user
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci_recursive(i), end=' ')








# Working with Fractions:
# Python provides a built-in fractions module to handle rational numbers and fractions.

# Example 1: Creating and performing arithmetic with fractions
from fractions import Fraction

# Create fractions
frac1 = Fraction(1, 2)  # 1/2
frac2 = Fraction(3, 4)  # 3/4

# Arithmetic operations
print(f"Sum: {frac1 + frac2}")          # Sum: 5/4
print(f"Difference: {frac1 - frac2}")   # Difference: -1/4
print(f"Product: {frac1 * frac2}")      # Product: 3/8
print(f"Division: {frac1 / frac2}")     # Division: 2/3

# Explanation:
# The Fraction class allows for easy creation and manipulation of fractions.
# You can perform operations like addition, subtraction, multiplication, and division.






# Example 2: Reducing a fraction to its simplest form
from fractions import Fraction

frac = Fraction(8, 12)  # 8/12
print(f"Simplified Fraction: {frac}")  # Output: 2/3

# Explanation:
# The Fraction class automatically simplifies fractions. For 8/12, it reduces the fraction to 2/3.





#  Converting floating-point numbers to fractions
from fractions import Fraction

float_num = 0.75
frac = Fraction(float_num).limit_denominator()
print(f"Fraction of {float_num}: {frac}")  # Output: 3/4

# Explanation:
# You can convert floating-point numbers to fractions using the Fraction() constructor.
# The limit_denominator() method can convert the float into its closest fractional form.








# Fibonacci Series
# Generate the first n terms of the Fibonacci sequence and find their sum.

def fibonacci_sum(n):
    a, b = 0, 1
    sum_fib = a + b
    print(a, b, end=' ')
    for i in range(2, n):
        c = a + b
        print(c, end=' ')
        sum_fib += c
        a, b = b, c
    print("\nSum of Fibonacci series:", sum_fib)

n = int(input("Enter the number of terms: "))
fibonacci_sum(n)

# Explanation:
# The function fibonacci_sum prints the Fibonacci series and calculates the sum of the numbers in the sequence.









# Taking number as input and printing it by multipling with 2. using function

values = []
def fun(values):
         if(i == 2): return(i+33)
         else: return i
        
num = int(input("Enter tottal number : "))
for i in range(num):
    a_num = int(input("Enter a number : "))
    values.append(a_num)

for i in values:
    pn = fun(values)
    print(pn, end=' ')
    
    
    
# avarage of some number

store = []
def avarages(store):
    sum = 0
    for i in store:
        sum = sum + i
    return sum
        
num = int(input("Enter total Number : "))
for i in range(num):
    numbers = int(input("Enter a number : "))
    store.append(numbers)
    
tot=avarages(store) 
print("Avarage : ", tot/len(store))   



