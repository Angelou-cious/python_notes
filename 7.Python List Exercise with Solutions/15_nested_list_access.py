# Given a nested list, print the element '55'.

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]] # This is the given nested list.

print(f'Original Lists: {nested_list}') # This line prints the original nested list.

find_55 = nested_list[1][1] # This line accesses the element '55' from the nested list.

print(find_55) # This line prints the found element.

# def get_specific_number(list1, find):

#     for i in list1:
#         if isinstance(i, list):
#             for j in i:
#                 if j == find:
#                     print(j)

# get_specific_number(nested_list, 55)
