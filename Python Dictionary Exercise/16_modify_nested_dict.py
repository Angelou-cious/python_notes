"""
    Exercise 16: Change value of a key in a nested dictionary

    Write a Python program to change Brad’s salary to 8500 in the following dictionary.

"""
def modify_nested_dict(dict1): # Define a function named modify_nested_dict that takes a dictionary as an argument.

    dict1['emp3']['salary'] = 8500 # Access the nested dictionary and change the value of the "salary" key for "emp3" to 8500.

    return dict1 # Return the modified dictionary.




sample_dict = { # Define a nested dictionary.
    'emp1': {'name': 'Jhon', 'salary': 7500}, # A key-value pair where the value is another dictionary.
    'emp2': {'name': 'Emma', 'salary': 8000}, # A key-value pair where the value is another dictionary.
    'emp3': {'name': 'Brad', 'salary': 500} # A key-value pair where the value is another dictionary.
}

x = modify_nested_dict(sample_dict) # Call the modify_nested_dict function with the sample_dict and store the returned dictionary in x.

print(x) # Print the modified dictionary.
