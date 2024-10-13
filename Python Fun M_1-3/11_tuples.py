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


 