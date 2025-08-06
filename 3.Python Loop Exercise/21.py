def flatten_list(lst):

    flat_list = []

    for item in lst:
        if type(item) == list:
            for i in item:
                flat_list.append(i)
        else:
            flat_list.append(item)
            
    flat_list.sort()
    return flat_list

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

# write function 'flatten_list' to flatten a nested list
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]