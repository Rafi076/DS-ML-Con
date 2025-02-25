


# Dic tionaries are ordered collection of data items.
# They store multiple items in a singel variable.
# Dictionary items are key value pairs that are separated by commas
# and enclosed within curly brackets.dictionaries store item inorder way!!

info = {
    'name':'rafi',
    'age': 24,
    'elibible':True,
    76:"mohin"
}
print(info["name"]) # rafi
print(info[76]) # mohin
print(info) # {'name': 'rafi', 'age': 24, 'elibible': True, 76: 'mohin'}
print(info.keys()) # (['name', 'age', 'elibible', 76])
# Or
for key in info.keys():
    print(info[key]) # rafi 24 True mohin
    
print(info.values()) # ['rafi', 24, True, 'mohin']
# Or
for key in info.keys():
    print(f"The values corresponding to the {key} is {info[key]}")

#The values corresponding to the name is rafi
# The values corresponding to the age is 24
# The values corresponding to the elibible is True
# The values corresponding to the 76 is mohin




# Creating a Dictionary
# 1. Empty dictionary
empty_dict = {}


# 2. Dictionary with some key-value pairs
student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}
# Accessing Elements
# Accessing values by key
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 25
# Using `.get()` to avoid KeyError if the key doesn’t exist
print(student.get("grade", "Not Available"))  # Output: Not Available




# 3. Using the `dict()` constructor
person = dict(name="Bob", age=30, profession="Engineer")

# 4. Nested dictionary
school = {
    "class_1": {"name": "John", "age": 12},
    "class_2": {"name": "Emma", "age": 13}
}

# Adding and Modifying Elements
# Adding a new key-value pair
student["grade"] = "A"
# Modifying an existing value
student["age"] = 26
print(student)  
# Output: 
#  {
# 'name': 'Alice', 
# 'age': 26, 
# 'major': 'Computer Science', 
# 'grade': 'A'
#  }



# Looping through a Dictionary
# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")


# Using Dictionaries with Functions
def print_student_info(info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_student_info(student)
# Output:
# name: Alice
# grade: A
# age: 27
# major: Physics





# Creating an empty dictionary
dictt = {}
# Creating a dictionary with key-value pairs
dictt = {
    'name':'Rafi',
    'age':25,
    'phone':'0121'
    }
print(dictt)
# Output: {'name': 'Rafi', 'age': 25, 'phone': '0121'}


# Accessing values using keys
name = dictt['name']
age = dictt.get('age')
print(name,age)
# Output: Rafi 25


# Adding new key-value pairs to the dictionary
dictt['job'] = 'Eng'
dictt['country'] = 'bd'
print(dictt)
# Output: {'name': 'Rafi', 'age': 25, 'phone': '0121', 'job': 'Eng', 'country': 'bd'}


# Deleting a key-value pair using del
del dictt['job']
print(dictt)
# Output: {'name': 'Rafi', 'age': 25, 'phone': '0121', 'country': 'bd'}


# Deleting a key-value pair using pop and returning the value
age = dictt.pop('age')
print(dictt)
# Output: {'name': 'Rafi', 'phone': '0121', 'country': 'bd'}


# Deleting the last inserted key-value pair using popitem and returning the key-value pair as a tuple
last_item = dictt.popitem()
print(dictt, last_item)
# Output: {'name': 'Rafi', 'phone': '0121'} ('country', 'bd')


# Updating the value of an existing key
dictt['age'] = 26
print(dictt)
# Output: {'name': 'Rafi', 'phone': '0121', 'age': 26}



# Iterating through the dictionary using items() to get key-value pairs
for key, value in dictt.items():
    print(key, value)
# Output:
# name Rafi
# phone 0121
# age 26


# Iterating through the dictionary using keys only
for i in dictt:
   print(i)
# Output:
# name
# phone
# age


# Iterating through the dictionary using values only
for i in dictt.values():
   print(i)
# Output:
# Rafi
# 0121
# 26


# Finding the length of the dictionary
length = len(dictt)
print(length)
# Output: 3


# Using built-in functions keys(), values(), and items()
key = dictt.keys()
value = dictt.values()
items = dictt.items()
print(key, value, items)
# Output: dict_keys(['name', 'phone', 'age']) dict_values(['Rafi', '0121', 26]) dict_items([('name', 'Rafi'), ('phone', '0121'), ('age', 26)])


# Updating the dictionary using update()
dictt.update({'job':'Eng','hobby':'reading'})
print(dictt)
# Output: {'name': 'Rafi', 'phone': '0121', 'age': 26, 'job': 'Eng', 'hobby': 'reading'}


# Membership test using in and not in
if 'salary' not in dictt:
    print('not found')
else:
    print('found')
# Output: not found


# Example of counting word occurrences using a dictionary
word = ['apple', 'banana','apple','orange','banana','apple']
word_count = {}
for i in word:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] += 1
print(word_count)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}




############### Dictionaries Method ######################
seniors = {222:98, 212:78, 312:95,132:77, 342:69}
juniors = {111:75, 333:47, 442:66, 553:78}
# seniors.update(juniors)
# print(seniors) # after updating: {222: 98, 212: 78, 312: 95, 132: 77, 342: 69, 111: 75, 333: 47, 442: 66, 553: 78}

seniors.pop(222) # to pop specific item
print(seniors) # {212: 78, 312: 95, 132: 77, 342: 69}

# to pop last item
seniors.popitem()
print(seniors) # {212: 78, 312: 95, 132: 77}

# to delete an item
del seniors[212]
print(seniors) # {312: 95, 132: 77}






# ***************************
# Counting the Frequency of Elements in a List
# Count the frequency of each element
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for item in elements:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}





# ****************************
# Nested Dictionary Example
# Dictionary with nested dictionaries
company = {
    "employee_1": {
        "name": "Alice", 
        "position": "Manager"
        },

    "employee_2": {
        "name": "Bob", 
        "position": "Developer"
        }
}

# Accessing nested elements
print(company["employee_1"]["name"])  # Output: Alice