"""
    Dictionary from Lists

    Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.

"""

# Define a list of string keys for the dictionary
keys = ['Ten', 'Twenty', 'Thirty']

# Define a list of integer values that correspond to the keys
values = [10, 20, 30]

# Initialize an empty dictionary to store the key-value pairs
new_dict = {}

# Use zip() to combine the keys and values lists into pairs
# Zip creates an iterator of tuples where each tuple contains
# one element from keys and the corresponding element from values
for key, value in zip(keys, values):

    # Assign each key-value pair to the dictionary
    # The current key is used as the dictionary key
    # The current value is assigned as the value for that key
    new_dict[key] = value

# Print the resulting dictionary showing the combined key-value pairs
print(f"{new_dict}")