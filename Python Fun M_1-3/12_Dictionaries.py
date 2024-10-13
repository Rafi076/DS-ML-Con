# Dic tionaries are ordered collection of data items.
# They dtore multiple items in a singel variable.
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