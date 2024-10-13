#sets are collection of data ietem. they store multiple in the singel variable. 
# set item are separated by commma & enclosed with curly{} brackets.set do not contain duplicate value.
# set are unchangeable.it sotore item unorderly!#
A_sets = {18,"rafi",12,18}
#print(set)
# OR
for i in A_sets:
    print(i,end=' ') # 18 12 rafi

# key & value in set
student = {
    "name" : "Rafi",
    "course": "Python",
    "Batch" : 1,
    "is_valid" : True,
}
print(student.get("is_valid", False))

for key, value in student.items():
    print("Key :", key  ,"vlaue :", value)






rafi = {} # it refer empty dictionary not empty set
print(type(rafi)) # <class 'dict'>  
# to creat empty set :
rafii = set()
print(type(rafii)) # <class 'set'>

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2)) # s1 U s2 = {1, 2, 3, 5, 6, 7}
s1.update(s2) # s1= {1, 2, 3, 5, 6, 7}
print(s1,s2) # s2 = {3, 6, 7}

s3 = {1,2,5,6}
s4 = {3,9,1,6,7}
s5 = s3.intersection(s4)
print("S5 = ",s5) # S5 =  {1, 6} --> common in both set
s6 = s3.symmetric_difference(s4)
print("S6 = ",s6) # S6 =  {2, 3, 5, 7, 9} --> which are not common in both set

#to check if two sets are dis joint :
print(s3.isdisjoint(s4)) # False

#to check if two sets are superset :
print(s3.issuperset(s4)) # False

#to check if two sets are subset :
print(s3.issubset(s4)) # False

# to add somthing on set use add():
contries = {"Bangladesh","UAE","China","Germany"}
contries.add("Pakistan")
print(contries) # {'Pakistan', 'China', 'Germany', 'Bangladesh', 'UAE'}

# same as remove/pop...
item = contries.pop()
print(item) #UAE : Randomly poped
print(contries) # {'China', 'Pakistan', 'Germany', 'Bangladesh'}

# # To delete a complete set we use del:
# contries2 = {"Bangladesh","UAE","China","Germany"}
# del contries2
# print(contries2) # Error

# # To not clear a complete set but to remove all item:
# contries2.clear()
# print(contries2) # Error

# to check any item on set:
if "Bangladesh" in contries:
    print("Yes exist") # Yes exist
else:
    print("Not exist")