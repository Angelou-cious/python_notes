"""
    Exercise 17: Invert Dictionary

    Write a code to swap keys and values in a dictionary. Assume all values are unique

    Original dictionary 1: {'a': 1, 'b': 2, 'c': 3}
    Inverted dictionary 1: {1: 'a', 2: 'b', 3: 'c'}

"""
def invert_dictionary(dict1):  # Define function to invert dictionary keys and values

    inverted_dictionary = {}  # Initialize empty dictionary to store inverted key-value pairs

    print(f'Original dictionary 1: {dict1}')  # Print the original dictionary

    for key, value in dict1.items():  # Iterate through each key-value pair in the original dictionary
        inverted_dictionary[value] = key  # Swap key and value - original value becomes new key, original key becomes new value
    
    print(f'Inverted dictionary 1: {inverted_dictionary}')  # Print the inverted dictionary



original_dict1 = {'a': 1, 'b': 2, 'c': 3}  # Create original dictionary with string keys and integer values

invert_dictionary(original_dict1)  # Call function to invert the dictionary