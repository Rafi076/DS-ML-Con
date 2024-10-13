# print(5+6) #addition
# print(15-6) #substract
# print(15*6) #multiplie
# print(15/6) #division
# print(15//6) #floor division
# print(5%3) #mod
# print(2**4) #exponential

import math
a = 1.7
b = 7.1
    #user input
# a = float(input("Enter a number for a: "))
# b = float(input("Enter a number for b: "))
print("Addition of a and b is =", a + b)
print("Subtraction of a and b is =", a - b)
print("Multiplication of a and b is =", round(a * b, 5))  # Round to 5 decimal places
print("Division of a and b is =", round(a / b, 4))  # Round to 4 decimal places
print("Exponential of a^b is =", round(a ** b, 6))  # Round to 6 decimal places
print("Modulus of a and b is =", a % b)
print("Ceil of (1.7 + 8) is =", math.ceil(1.7 + 8))  # Ceil function
print("Floor of (1.7 + 8) is =", math.floor(1.7 + 8))  # Floor function


# To handel string 

# accessing string as array
name = "mohin_rafi"
print(len(name)) # 10
# print(name[2]) # print = h
# print(name[3]) # print = i
# print(name[1:4]) # print = ohi

# another way is using loop
print("printing using loop: ")
for character in name:
 print(character)
 
# magic in python
author = "Jack"
age = 32
fruit = "Mango"
home = "NYC"

st = "A new megajin that come to news was written by",author,". He is ",age," years old .",fruit," is his favourite fruits!!."
print(st)
print(len(st))

another_str = "!!hello Rafi this is long time ago!!!"
print(another_str.upper()) # HELLO RAFI THIS IS LONG TIME AGO!

# to restrip "mark" like : !!
print(another_str.rstrip("!")) # !!hello Rafi this is long time ago
print(another_str.replace("Rafi","Jhon")) # !!hello Jhon this is long time ago!!! (replace all rafi)
# to create a list we use split( for : !!hello Rafi this is long time ago!!! )
print(another_str.split()) # ['!!hello', 'Rafi', 'this', 'is', 'long', 'time', 'ago!!!']
# to capitalize heading first word
let_str = "hello Rafi this is long time ago!!!"
print(let_str.capitalize()) # Hello rafi this is long time ago!!!
# to centarized a string to any position
print(len(let_str)) #35
print(let_str.center(37)) 
print(len(let_str.center(37))) # 37
print(let_str.count("Rafi")) # to count specific word
#to find if a string ending with specific word
print(let_str.endswith("!")) # true
# to find if a secific word is ending in the secific range of a string
print(let_str.endswith("this",7,16))
print(let_str.find("Rafi")) # 6, if rafi not in index return -1

let_str1 = "hello Rafi this is long time ago"
let_str2 = "Hello"
# checks if all the characters in the given string are alphanumeric (consisting of letters A-Z, a-z, and/or digits 0-9) and if the string is not empty. If the string contains any characters other than alphanumeric ones, it returns False.
print(let_str1.isalnum()) # The output will indeed be False because the string contains spaces and does not consist solely of alphanumeric characters. 

# checks if all the characters in the given string are alphabetic (consisting only of letters A-Z or a-z) and if the string is not empty. If the string contains any characters other than letters, it returns False..
print(let_str1.isalpha()) # The output will be False because the string contains spaces and is not composed solely of alphabetical characters.
print(let_str2.isalpha()) # true

# to check all case is in lower
print(let_str1.islower()) #false

#to check if string is only white space
white_string = "    " 
print(white_string.isspace()) # True

#to check if a string start with specific word
print(let_str1.startswith("hello")) # true

# to swap all upper case to lower case
print(let_str1.swapcase()) # HELLO rAFI THIS IS LONG TIME AGO

# to convert every character of every word in string to upper case
print(let_str1.title()) # Hello Rafi This Is Long Time Ago


 
