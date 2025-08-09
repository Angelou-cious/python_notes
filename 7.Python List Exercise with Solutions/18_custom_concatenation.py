
# Exercise 18: Concatenate two lists in the following order

def concat_lists(lists1,lists2):

    merge_lists = []

    for i in lists1:
        for j in lists2:
            merge_lists.append(i + j)
    return merge_lists


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

x = concat_lists(list1, list2)
print(x)