#  Shopping List Manager:
# You are asked to create a shopping List Manager.
# The user can add item to the shopping List when "done" is typed,
# then the input System close & you need to display the list along 
# with the total number of item.

shoppingList = []
while True:
    item = input("Enter The Item : ")
    shoppingList.append(item)
    if item == "done":
        shoppingList.pop()
        break

# print(shoppingList)
# Display the final shopping list and total number of items
print("\nYour Shopping List:")
for i, item in enumerate(shoppingList, 1):
    print(f"{i}.  {item}")









