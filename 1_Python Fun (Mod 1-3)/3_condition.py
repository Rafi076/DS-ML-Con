

# Simple condition in PY
var = int(input("Enter a number : ") )
if(var>5 and var<20):
    print("Under 5 to 10")
elif(var>=21 and var<=45):
    print("Under 21 to 45")
else:
    print("Not acceptable")

print("Finished")





# creating international clock:
import time
clock = time.strftime('%H:%M:%S')
print("Current Time : ", clock)
hour = int(time.strftime('%H')) # string should convert to intiger!!
# min = int(time.strftime('%M'))

if( 0 <= hour < 6):
    match hour:
        case 0: 
            string = "it is bed time"
            print(' '.join(char for char in string)) # to print in same line
            
        case _ if (1<= hour <= 4) : # used with condition
            string = "Dark mid night" 
            print(' '.join(char for char in string)) # used loop
            
        case _: print("Time to wake up") # case_: used as default
        

elif(6 <= hour < 11): 
    match hour:
        case 6: print("Wake up")
        case _ if(7<= hour <= 10) : print("Complite Breakfast") # used with condition
        case _: print("sun up!") # case_: used as default
        
elif(11 <= hour < 18): 
    match hour:
        case 11: print("After Noon Time")
        case _ if (12<= hour < 18) : print("Lunch Time") # used with condition
        case _: print("sun Down!") # case_: used as default


elif(18 <= hour < 23): 
    match hour:
        case _ if (18 <= hour < 22):  # You can use an underscore (`_`) for the match if it's a range check
            print("Evening Time")
        case 22:  # You are specifically checking for hour 22 (10 PM)
            print("Dinner Time")
        case _: 
            print("Sun Down already!")  # Default case for anything outside the previous conditions

else: 
    match hour:
        case 18: print("After Noon Time")
        case _ if (19<= hour < 22) : print("Getting Night") # used with condition
        case 22 if (22 <= hour <= 24):  # case_: used as default
            string = "Ending today soon"
            print(' '.join(char for char in string)) # used loop
    
    
    
    
    
    
    
# in Loop seacial
color = ["red","green","blue","Yellow"]
for color in color:
    print(color.center(50))
    for i in color:
     print(i.center(50))
     
     
     
# range printing in loop
for i in range(2,10): 
    print(i,end=' ')

print('\n\n')


# to print 1 to 15 incrementing 2
for k in range(1,15,2):
    if k%2!=0:
        print(k,end=' ')
    else: print("No")



# Python Conditions: A Comprehensive Guide
# In Python, conditions are expressions used to make decisions based on different outcomes. The basic building blocks for conditions are the comparison and logical operators, combined with control flow structures like if, elif, and else.



# 1. Comparison Operators
# Comparison operators compare two values and return either True or False. These are often used in condition expressions.

# Operator	Meaning	Example
# ==	Equal to	x == y
# !=	Not equal to	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y
# Example:
# python
# code

x = 10
y = 5
if x > y:
    print("\nx is greater than y")


# 2. Logical Operators
# Logical operators combine multiple conditions.

# Operator	Meaning	Example
# and	True if both conditions are true	x > 5 and y < 10
# or	True if at least one condition is true	x > 5 or y < 3
# not	Reverses the result of the condition	not(x == y)
# Example:
# python
# Copy code

x = 5
y = 10
if x > 0 and y > 0:
    print("Both numbers are positive")



# 3. Control Flow Structures
# if statement: Checks a condition, runs the indented block if the condition is True.
# elif statement: Stands for "else if," checks multiple conditions after an if fails.
# else statement: Executes if none of the above conditions are true.
# Example:
# python
# Copy code

x = 7
if x > 10: print("x is greater than 10")
elif x == 7: print("x is 7")
else: print("x is less than 10 and not 7")




# 4. Ternary Operator (Conditional Expressions)***********************************
# Python supports a shorthand if-else called the ternary operator.

# Syntax:
# result = value_if_true if condition else value_if_false

# Example:
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult




# 5. Multiple Conditions (Chaining Conditions)
# Python allows conditions to be chained for better readability.

# Example:
# python
# Copy code

x = 5
if 1 < x < 10:
    print("x is between 1 and 10")



# 6. Checking Membership
# You can check if a value is part of a list, tuple, or set using in.

# Example:
# python
# Copy code

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")




# 7. Checking Identity
# Use is to compare if two variables point to the same object.

# Example:
# python
# Copy code

a = [1, 2, 3]
b = a
if a is b:
    print("a and b refer to the same object")



# Summary
# Python conditions can be written using comparison and logical operators, and controlled using if, elif, and else statements. Additionally, Python supports more advanced features like ternary operators, membership checking, and identity checking for building more complex decision-making code.

# This short overview provides you with the essentials to write and use conditions effectively in Python.

# Complete Example:
# python
# Copy code

x = 20
y = 15
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is less than {y}")

# Ternary operator
is_even = "Even" if x % 2 == 0 else "Odd"
print(f"x is {is_even}")
