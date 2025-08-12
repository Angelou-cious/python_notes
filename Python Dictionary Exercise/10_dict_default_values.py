"""
    Exercise 10: Initialize dictionary with default values

    In Python, we can initialize the keys with the same values.

    {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
"""
# my code
def mod_dict(a, b):    # Define function to create dictionary from list and default values
    new_dict = {}      # Initialize empty dictionary

    for item in a:      # Iterate through each item in input list
        new_dict[item] = b  # Assign default value to each key
    return new_dict     # Return the populated dictionary

employees = ['Kelly', 'Emma']  # List of employee names
defaults = {"designation": 'Developer', "salary": 8000}  # Default values dictionary

x = mod_dict(employees, defaults)  # Create dictionary using the function

print(x)  # Print the resulting dictionary


# best performance
employees = ['Kelly', 'Emma', 'John']  # Create list of employee names
defaults = {"designation": 'Developer', "salary": 8000}  # Define default values dictionary

res = dict.fromkeys(employees, defaults)  # Create dictionary with employee names as keys and defaults as values

print(res)  # Print the resulting dictionary with default values