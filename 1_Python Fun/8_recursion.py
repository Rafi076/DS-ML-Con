# Python Recursion - A Quick Guide
# Recursion is a method of solving problems where a function calls itself. It breaks a problem into smaller subproblems, each of which is a simpler instance of the original problem.

# Key Components of Recursion:
# Base Case: A condition to stop the recursion (prevents infinite calls).
# Recursive Case: The part of the function where it calls itself with modified arguments.






# Basic Structure:

def recursive_function(parameters):
    if base_case_condition:
        return base_case_value
    else:
        return recursive_function(modified_parameters)








# Print 1 to n using Recursion
def print_1_to_n(n):
    if n > 0:
        print_1_to_n(n-1)
        print(n, end=' ')  # Print after the recursive call to print in ascending order

n = int(input("Enter a number: "))
print_1_to_n(n)






# Print n to 1 using Recursion
def print_n_to_1(n):
    if n > 0:
        print(n, end=' ')  # Print before the recursive call to print in descending order
        print_n_to_1(n-1)

n = int(input("Enter a number: "))
print_n_to_1(n)






# Pyramid Pattern using Recursion
def pyramid(n, current=1):
    if current <= n:
        print(' ' * (n - current) + '* ' * current)
        pyramid(n, current + 1)

n = int(input("Enter the number of levels: "))
pyramid(n)






# Inverted Pyramid Pattern using Recursion
def inverted_pyramid(n):
    if n > 0:
        print(' ' * (5 - n) + '* ' * n)
        inverted_pyramid(n - 1)

n = int(input("Enter the number of levels: "))
inverted_pyramid(n)






# Vowel Count using Recursion
def count_vowels(s, i=0):
    vowels = "aeiouAEIOU"
    if i == len(s):
        return 0
    return (1 if s[i] in vowels else 0) + count_vowels(s, i+1)

s = input("Enter a string: ")
vowel_count = count_vowels(s)
print("Number of vowels:", vowel_count)






# Find Maximum Number using Recursion
def find_max(lst, n):
    if n == 1:
        return lst[0]
    return max(lst[n-1], find_max(lst, n-1))

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
max_value = find_max(lst, len(lst))
print("Maximum number:", max_value)






# Summation of Numbers from 1 to n using Recursion
def summation(n):
    if n == 0:
        return 0
    return n + summation(n - 1)

n = int(input("Enter a number: "))
total_sum = summation(n)
print("Sum from 1 to", n, ":", total_sum)





# Summation of List Elements using Recursion
def sum_list(lst, n):
    if n == 0:
        return 0
    return lst[n-1] + sum_list(lst, n-1)

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
total_sum = sum_list(lst, len(lst))
print("Sum of list elements:", total_sum)







# factorial of a number using recursion

def factorial(num):
    if(num == 1 or num == 0): return 1
    else: return(factorial(num-1)*num)

num = int(input("Enter a number : "))
x = factorial(num)
print(f"Factorial of {num} is = ",x)






# Fibonacci serices: 
def fibonacci(num):
    fib_serices = [0,1]
    while len(fib_serices)<num:
        fib_serices.append(fib_serices[-1]+fib_serices[-2])
    return fib_serices

num = int(input("Enter a number for fibonacci serices : "))
result = fibonacci(num)
print(result)





