
"""
    Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
"""

def merge_lists(lst1,lst2):

    merge_list = []

    for a, b in zip(list1, list2):
        res = a + b
        merge_list.append(res)
    return merge_list

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

results = merge_lists(list1, list2)

print(results) # ['My', 'name', 'is', 'Kelly']