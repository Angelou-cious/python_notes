

# Write a function to flatten a list of lists into a single, non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]

flatten_list = []

for item in list_of_lists:
    if type(item) == list:
        for i in item:
            flatten_list.append(i)
    else:
        flatten_list.append(item)

print(flatten_list)