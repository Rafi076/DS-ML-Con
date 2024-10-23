# Write a Program to sort by ascending order from the following list. (Create a function to solve it)
# List = [1,5,2,9,3,22,13]


# # Using Built function
def sort_list(lst):
    return sorted(lst)

list = [1, 5, 2, 9, 3, 22, 13]

sorted_list = sort_list(list)
print("Sorted List:",sorted_list)




# Without built function
def sort_list(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

list = [1, 5, 2, 9, 3, 22, 13]

sorted_list = sort_list(list)
print("Sorted List:",sorted_list)