def flatten_list(list_input): # Define a function named flatten_list that takes a list as input

    flatten_list = [] # Initialize an empty list to store the flattened elements

    for item in list_input: # Iterate through each item in the input list
        if type(item) == list: # Check if the item is a list
            for i in item: # If it's a list, iterate through its elements
                flatten_list.append(i) # Append each element to the flatten_list
        else: # If the item is not a list
            flatten_list.append(item) # Append the item directly to the flatten_list

    flatten_list.sort() # Sort the flattened list in ascending order
    return flatten_list # Return the sorted flattened list



nested_list = [1, [3, 2], [4, 5, 6], 7, [9, 8]] # Define a nested list

flattened = flatten_list(nested_list) # Call the flatten_list function with the nested_list
print("Flattened list:", flattened) # Print the flattened list
