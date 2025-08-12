"""
    Exercise 13: Check if a value exists in a dictionary

    While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.

    Write a Python program to check if the value 200 is present in the provided dictionary.

    200 present in a dict

"""
def is_present(dict1, to_find):  # Define function to check if a value exists in dictionary

    for item in dict1.values():  # Iterate through all values in the dictionary
        if item == to_find:  # Check if current value matches the value we're looking for
            return [True, to_find]  # Return True and the found value if match is found
    
    return [False, to_find]  # Return False and the searched value if no match is found

sample_dict = {'a': 100, 'b': 200, 'c': 300}  # Create sample dictionary with key-value pairs

result = is_present(sample_dict, 20)  # Call function to check if value 20 exists in dictionary

if result[0]:  # Check if the first element (boolean) is True
    print(f'{result[1]} present in a dict')  # Print message if value is found
else:  # If the first element is False
    print(f'{result[1]} not present')  # Print message if value is not found
    


