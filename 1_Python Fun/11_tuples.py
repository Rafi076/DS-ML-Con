# prompt: is list , tuple, set  .. mutable,order, duplicte allow?

# | Feature       | List      | Tuple     | Set       |
# |---------------|-----------|-----------|-----------|
# | Mutable       | Yes       | No        | Yes       |
# | Ordered       | Yes       | Yes       | No        |
# | Duplicates    | Yes       | Yes       | No        |



# prompt: Tuples exampl

password = ("my_secret_password",)
print(password[0])  # Output: my_secret_password
user_credentials = ("john_doe", "password123")
username, password = user_credentials
print(f"Username: {username}, Password: {password}")



mixed_set = {1,'hi',23,4}
print(mixed_set) # unorderd print


num = {1,3,5,1,4}
print(num) # dont print duplicate value



# prompt: covert a list to set then again in set to remove duplicate value

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
my_new_list = list(my_set)
print(my_new_list)




# prompt: discard & remove work same

my_set = {1, 2, 3}

# Using remove()
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# Using remove() on a non-existent element
# my_set.remove(4)  # Raises a KeyError

# Using discard()
my_set.discard(3)
print(my_set)  # Output: {1}

# Using discard() on a non-existent element
my_set.discard(4)  # Does nothing, no error is raised
print(my_set)  # Output: {1}





# prompt: | , & in set

# Set Operations: Union, Intersection, Difference

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (|) - Combines elements from both sets without duplicates
union_set = set1 | set2
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection (&) - Returns common elements between sets
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3}

# Difference (-) - Returns elements in the first set but not in the second
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)  # Output: {1, 2}

difference_set = set2 - set1
print("Difference (set2 - set1):", difference_set)  # Output: {4, 5}


set1 = {1,2,3}
set2 = {3,4,5}
unionofset = set1|set2
print(unionofset)


common = set1 & set2
print(common)


unique_to_set1 = set1 - set2
print(unique_to_set1)




# Create a set of squares of numbers from 1 to 10 using set comprehension
squares = {x**2 for x in range(1, 11)}
print(squares)

# Create a set of even numbers from a list using set comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)

# Create a set of unique characters from a string using set comprehension
string = "hello world"
unique_characters = {char for char in string}
print(unique_characters)




# Assingment 2:

my = {'ctg','srimongal','dhaka'}
frnd = {'ctg','khulna','dhaka'}

intersection_set = my & frnd
print("Intersection:", intersection_set)
print("Only i Visited: ",my - frnd)
print("Only frnd Visited: ",frnd -my)

# Intersection: {'dhaka', 'ctg'}
# Only i Visited:  {'srimongal'}
# Only frnd Visited:  {'khulna'}



# tuples are ordered collection of data item. they store multiple item in a single variable.
# tuple item are separated by comma and enclosed within round brackets ()
# tupels are unchangeable meaning we can not alter them after creation like list
tup = (1,"GREEN",4,7,"black")
print(type(tup),tup) # <class 'tuple'> (1, 'GREEN')
print(tup[0]) # 1

if "GREEN" in tup:
    print("yes")
    tup2 = tup[1:3]
    print(tup2,end=' ') # ('GREEN', 4)
    
else: print("no")

# tup[0] = (90,) # can not change tuple
# print(type(tup),tup) # WRONG!

##  Tuples are immutable, hence if you want to add, remove or change tuple item,
##  then first you must convert the tuple to a list. then perform operation on that
##  list and convert it back to tuple

# # to manipulating tuples ##
countries = ("spain", "Italy", "India", "England", "Germany",1,2,3,2,4,5,3,2,6,2,1)
temp = list(countries)
temp.append("Bangladesh") # add item
temp.pop(2)               # remove item
temp[2] = "UAE"           # change item
countries = tuple(temp)
print(countries)          # ('spain', 'Italy', 'UAE', 'Germany', 1, 2, 3, 2, 4, 5, 3, 2, 6, 2, 1, 'Bangladesh')

To_count_a_item = countries.count(2)
print("item 2 is times : ",To_count_a_item) # item 2 is times :  4
index_of_two = countries.index(2)
print("first index of 2 is : ",index_of_two) # 5
index_of_two_from_index_8_to_15 = countries.index(2,8,15)
print("index_of_two_from_index_8_to_15 : ",index_of_two_from_index_8_to_15) # index_of_two_from_index_8_to_15 :  11


# Repetition:
repeated_tuple = ('A',) * 3
print(repeated_tuple)  # Output: ('A', 'A', 'A')


# index(element): Returns the index of the first occurrence of the element.
my_tuple = (10, 20, 30, 20)
print(my_tuple.index(20))  # Output: 1


# Swapping Two Variables Using Tuples
# Swapping values without a temporary variable
a = 5
b = 10
# Packing and unpacking
a, b = b, a
print(f"a = {a}, b = {b}")  # Output: a = 10, b = 5



# Tuple Unpacking
# Unpacking a tuple into variables
person = ("Alice", 25, "Engineer")
name, age, profession = person

print(name)       # Output: Alice
print(age)        # Output: 25
print(profession) # Output: Engineer