"""
    You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
"""

def replace_list_item(lst):
    # print the expected output
    print(f'Expected Output: [5, 10, 15, 200, 25, 50, 20]')

    # get the index of the first occurrence of 20 in the list
    index = lst.index(20) # get the index of the first find

    # replace the value at the index with 200
    lst[index] = 200

    # return the modified list
    return lst


# test the function with a sample list
list1 = [5, 10, 15, 20, 25, 50, 20]    

# print the modified list
print(replace_list_item(list1))
