a = 3000
b = 300
print("A") if a>b else print("=") if a==b else print("B")


# Checking if a number is even or odd using a ternary operator
num = 4
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Even


# Assigning value based on a condition
age = 20
category = "Adult" if age >= 18 else "Minor"
print(category)  # Output: Adult



# Nested ternary operator to find the maximum of three numbers
x = 5
y = 10
z = 7

max_value = x if x > y and x > z else y if y > z else z
print(max_value)  # Output: 10



# #example:
# result = value_if_true if conditon else value_if_false
# # this syntax is equivalent to the following if else statment

# if condition:
#     result = value_if_true
# else:
#     result = value_if_false