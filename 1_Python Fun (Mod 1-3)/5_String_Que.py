 #  ******************************* SOME PROBLEM SOLVING FOR STRING *************************************


# Problem 1: Check if a String is a Palindrome---
# A palindrome is a word or phrase that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

def is_palindrome():
    # Get input from the user
    s = input("Enter a string: ")
    
    # Convert the string to lowercase and remove non-alphanumeric characters
    s_cleaned = ''.join(char.lower()   for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    if s_cleaned == s_cleaned[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Call the function
is_palindrome()

# OUTPUT:
# Enter a string: Madam
# The string is a palindrome.

# Enter a string: Hello
# The string is not a palindrome.






# Problem 2: Count the Occurrence of Each Character in a String---
# Count how many times each character appears in a string.

from collections import Counter

def char_count():
    # Get input from the user
    s = input("Enter a string: ")
    # Return the count of each character
    return Counter(s)

# Call the function and print the result
print(char_count())

# OUTPUT : 
# Enter a string: hello world
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})









# Problem 3: Reverse the Words in a Sentence---
# Reverse the words in a sentence, but the order of the characters in each word should remain the same.

def reverse_words():
    # Get input from the user
    sentence = input("Enter a sentence: ")
    # Split the sentence into words and reverse them
    return ' '.join(reversed(sentence.split()))

# Call the function and print the result
print(reverse_words())

# OUTPUT :
# Enter a sentence: Python is fun
# fun is Python






# Problem 4: Remove All Vowels from a String---
# Write a function that removes all vowels (a, e, i, o, u) from a given string.

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])

# Test
print(remove_vowels("Beautiful Day"))  

# Output: "Btfl Dy"





# Problem 5: Capitalize the First Letter of Each Word
# Write a function that capitalizes the first letter of each word in a string.

def capitalize_words(s):
    return s.title()

# Test
print(capitalize_words("this is a test sentence"))  

# Output: "This Is A Test Sentence"