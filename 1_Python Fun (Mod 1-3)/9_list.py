#  rest of the item in set
bazarer_list = [
    "chini",
    "lobon",
    "Morich",
    "ada",
    "Darchini",
]

first_item, secound_itemm, *rest_of_the_item = bazarer_list
print(first_item)
print(secound_itemm),
print(rest_of_the_item)
# output: 
# chini
# lobon
# ['Morich', 'ada', 'Darchini']




# to find the specific item from the list 
color = ["green","red","white","blue","black","purpale"]
for i in range(len(color)):
    if(color[i]=="red"): 
        print(color[i],"found at index ",i)
    else: 
        print("Good to go!!")
        
        




# to find the specific item from the list 
# List of colors
colors = ["green", "red", "white", "blue", "black", "purple"]

# Loop through the list and find 'red'
for i in range(len(colors)):  # Using the length of the list
    if colors[i] == "red":  # Check if the item is 'red'
        print(colors[i], "found at index", i)
    else:
        print("Not red. Good to go!!")




# Checking if a substring is present in the list
# List of colors
colors = ["green", "red", "white", "blue", "black", "purple"]

# Check if any color contains the substring 'bg'
for i in range(len(colors)):
    if "bg" in colors[i]:  # Check if "bg" is part of the color name
        print(colors[i], "found at index", i)
    else:
        print("Good to go!!")




# Checking if a specific item exists in the list
color1 = ["green", "red", "white", "blue", "black", "purple"]

# Check if 'yellow' is in the list
if "yellow" in color1: 
    print("Yes, yellow is in the list")
else:
    print("No, yellow is not in the list")

# OR
color1 = ["green","red","white","blue","black","purpale"]
if "yallow" in color1: print("Yes")
else:print("No")





# List slicing allows you to extract parts of a list.

# List slicing examples
color1 = ["green", "red", "white", "blue", "black", "purple"]

# Print colors from index 1 to 3
print(color1[1:4])  # Output: ['red', 'white', 'blue']

# Print every second color starting from the first
print(color1[0:6:2])  # Output: ['green', 'white', 'black']







# to add in list
# Add 'pink' to the list
color1.append("pink")
print(color1)  # Output: ['green', 'red', 'white', 'blue', 'black', 'purple', 'pink']





# Sorting and Reversing a List
alist = [11, 12, 3, 2, 33, 4, 6, 21, 5]

# Sort the list
alist.sort()
print(alist)  # Output: [2, 3, 4, 5, 6, 11, 12, 21, 33]

# Reverse the list
alist.reverse()
print(alist)  # Output: [33, 21, 12, 11, 6, 5, 4, 3, 2]



# Finding the index of an element
print(alist.index(6),end='') # 4





# Copying a list
# Copying list 'new' into 'district'
district = ["dhaka", "chittagong", "khulna"]
new = ["sylhet", "rangpur", "barishal"]

district = new.copy()
print(district)  # Output: ['sylhet', 'rangpur', 'barishal']






# # to insert chittagong between syllhat and rangpur
# Insert 'chittagong' between 'sylhet' and 'rangpur'
district.insert(1, "chittagong")
print(district)  # Output: ['sylhet', 'chittagong', 'rangpur', 'barishal']





# #  Extending a list by combining two lists
district1 = ["dhaka", "chittagong", "khulna"]
new1 = ["sylhet", "rangpur", "barishal"]

# Extend district1 by adding elements from new1
district1.extend(new1)
print(district1)  # Output: ['dhaka', 'chittagong', 'khulna', 'sylhet', 'rangpur', 'barishal']
 





# Additional List Operations You Can Try:
# Removing an Element:

# Remove 'red' from the list
colors.remove("red")
print(colors)  # Output: ['green', 'white', 'blue', 'black', 'purple', 'pink']


# Pop Element from List:
# Pop removes and returns the last item or a specific index
last_item = colors.pop()
print(last_item)  # Output: 'pink'
print(colors)     # Output: ['green', 'white', 'blue', 'black', 'purple']



# Clear a List:
# Clear the entire list
colors.clear()
print(colors)  # Output: []




# Summary of Key List Functions:
# append(): Adds an item to the end of the list.
# extend(): Adds all items of a list (or any iterable) to another list.
# insert(): Inserts an item at a given position.
# remove(): Removes the first item with the specified value.
# pop(): Removes and returns an item from the list.
# clear(): Removes all elements from the list.
# index(): Returns the index of the first item with the specified value.
# sort(): Sorts the list in ascending order.
# reverse(): Reverses the elements of the list.





# ## KBC game -- Let’s walk through a simple quiz game using lists:##

quetions = [
    ["Which language was used to create fb ?","Python","JS","php","None",1],
    ["What is the capital of Bangladesh ?","Chittagon","khulna","Dhaka","syllhat",2],
    ["What is the addition of 1+1 = ?","01","1","2","10",3]
]
levels = [1000,2000,3000,4000,5000,6000,7000,8000]
money = 0
for i in range(0,len(quetions)):
    quetion = quetions[i]
    print(f"\nQuetion for tk.{levels[i]}")
    print(f"Q:{quetion[0]}")
    print(f"a.{quetion[1]}     b.{quetion[2]}")
    print(f"c.{quetion[3]}       d.{quetion[4]}")
    replay = int(input("Enter your answer (1-4): "))
    if(replay == quetion[-1]):
        print(f"Correct answer! you won tk- {levels[i]}")
        if(levels == 4): 
            money = 3000
        elif(levels == 6): 
            money = 4000
    else:
        print("wrong answer!")
        break
