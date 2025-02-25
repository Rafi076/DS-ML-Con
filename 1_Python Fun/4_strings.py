# Whenever string literals are present just after the definition of a function,
# module, class or method, they are associated with the object their doc-attribute.
# we can later use this attribute to retrieve this docstring.
name = "Rafi"
age = 24
prices = 2.56754
txt = f"Hello im {name}. im {age} year old.Today's meat prices is {prices:.3f}"
print(txt)



def square(n):
    '''Take a number n, returns the square of n'''  # This is a docstring
    print(n**2)  # Prints the square of the number

square(5)  # Calls the function with n=5, prints 25
print(square.__doc__)  # Prints the docstring of the square function

# OUTPUT:
# 25
# Take a number n, returns the square of n


    
# PEP 8:
# it stand for python Enhancement Proposal. it is a document that provide guidlines and best
# practices on hoe to write python code.







# Python Strings: A Comprehensive Guide
# In Python, strings are sequences of characters enclosed in single quotes ' ', double quotes " ", or triple quotes ''' ''' or """ """. They are one of the most commonly used data types in Python.

# 1. String Creation
# You can create strings using:

# Single quotes: 'Hello'
# Double quotes: "Hello"
# Triple quotes: '''Hello''' or """Hello"""
# Example:

string1 = 'Hello'
string2 = "World"
multiline_string = '''This is a multi-line string.'''






# 2. String Concatenation and Repetition
# Concatenation: Combine two or more strings using the + operator.
# Repetition: Repeat a string multiple times using the * operator.
# Example:

greet = "Hello, " + "World!"
repeat_str = "Python " * 3
print(greet)      # Output: Hello, World!
print(repeat_str) # Output: Python Python Python




# 3. String Indexing and Slicing
# Indexing: Access a character at a specific position using square brackets []. Indexing starts at 0.
# Slicing: Extract a part of a string using [start:end]. The end index is exclusive.
# Example:

text = "Python"
print(text[0])    # Output: P
print(text[-1])   # Output: n (negative indexing starts from the end)

# Slicing
print(text[1:4])  # Output: yth (from index 1 to 3)
print(text[:3])   # Output: Pyt (start to index 2)
print(text[3:])   # Output: hon (from index 3 to end)





# 4. String Methods
# Python provides a wide variety of built-in string methods. Some commonly used ones are:

# upper(): Converts all characters to uppercase.
# lower(): Converts all characters to lowercase.
# strip(): Removes leading and trailing spaces.
# replace(old, new): Replaces all occurrences of old with new.
# split(delimiter): Splits a string into a list based on the delimiter.
# join(iterable): Joins a list or iterable into a single string using a delimiter.
# Example:

text = "  Python is fun  "

print(text.upper())        # Output: "  PYTHON IS FUN  "
print(text.lower())        # Output: "  python is fun  "
print(text.strip())        # Output: "Python is fun" (spaces removed)
print(text.replace("fun", "awesome"))  # Output: "  Python is awesome  "
print(text.split())        # Output: ['Python', 'is', 'fun'] (default delimiter is space)
words = ['Python', 'is', 'cool']
print(' '.join(words))     # Output: "Python is cool"





# 5. String Formatting
# Python supports several ways to format strings:

# (1). Using + for Concatenation:
name = "Rafi"
age = 24
print("My name is " + name + " and I am " + str(age) + " years old.")


# (2). Using format():
name = "Rafi"
age = 24
print("My name is {} and I am {} years old.".format(name, age))


# (3). Using f-strings (Python 3.6+):
name = "Rafi"
age = 24
print(f"My name is {name} and I am {age} years old.")





# 6. String Escape Characters
# Escape characters allow special characters to be used within strings.

# Escape Character	     Description	               Example

#     \'	            Single quote	           'It\'s okay'
#     \"	            Double quote	        "She said, \"Hello!\""
#     \\	             Backslash	             'C:\\Program Files'
#     \n	             New line	               'Hello\nWorld'
#     \t	              Tab	                   'Hello\tWorld'

# Example:
print('It\'s a wonderful day!')
print("She said, \"Python is fun!\"")
print("Line 1\nLine 2")




# 7. String Length and Membership Operators
# len(): Returns the length of a string.
# in: Checks if a substring exists in the string.
# Example:
text = "Python is awesome"
print(len(text))       # Output: 17
print('Python' in text)  # Output: True
print('Java' in text)    # Output: False




# 8. String Immutability
# Strings in Python are immutable, meaning once a string is created, it cannot be modified. Instead, operations like replace() or concatenation return a new string.

# Example:
text = "Hello"
# text[0] = 'h'  # This will raise an error, as strings are immutable
new_text = 'h' + text[1:]  # This creates a new string
print(new_text)  # Output: hello





# 9. Multiline Strings
# Multiline strings can be created using triple quotes (''' or """), and they allow strings to span multiple lines.

# Example:
multiline_str = '''This is a multiline string.'''
print(multiline_str)




# 10. Raw Strings
# Raw strings treat backslashes (\) as literal characters and do not escape them. Raw strings are useful when dealing with file paths, regex, etc.

# Example:
raw_str = r'C:\Users\Rafi\Documents'
print(raw_str)  # Output: C:\Users\Rafi\Documents




# 11. Checking String Content
# Python provides methods to check the nature of a string's content:

# isalpha(): Returns True if all characters are alphabets.
# isdigit(): Returns True if all characters are digits.
# isalnum(): Returns True if all characters are alphanumeric.
# isspace(): Returns True if the string contains only whitespace.
# Example:
#
text = "Python3"
print(text.isalpha())  # Output: False (because '3' is a digit)
print(text.isalnum())  # Output: True
print("123".isdigit())  # Output: True
print("   ".isspace())  # Output: True


# Summary of Key String Methods

#   Method	                    Description	                                             Example

#   upper()	            Converts all characters to uppercase	                "python".upper() → "PYTHON"
#   lower()	            Converts all characters to lowercase	                "PYTHON".lower() → "python"
#   strip()	            Removes leading and trailing spaces	                    " python ".strip() → "python"
#   replace()	        Replaces a substring with another substring	            "python".replace("p", "P") → "Python"
#   split()	            Splits a string into a list	                            "a,b,c".split(",") → ['a', 'b', 'c']
#   join()	            Joins elements of a list into a string	                ",".join(['a', 'b', 'c']) → "a,b,c"
#   format()	        Formats a string	                                    "Hello {}".format("World") → "Hello World"
#   len()	            Returns the length of the string	                            len("Python") → 6
#   in	                Checks if a substring exists in a string	                  "Py" in "Python" → True



# By understanding these basic and advanced string manipulations in Python, you can handle text data effectively in any Python project.















    