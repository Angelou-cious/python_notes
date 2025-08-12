"""
    Perform basic dictionary operations:

    Perform following operations on given dictionary

    Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
    Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
    Access Key: Print the value associated with the city key.

    Expected Output:

    Original dictionary: {'name': 'Alice', 'age': 35, 'city': 'New York'}

    Updated dictionary after adding 'profession': {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

    Updated dictionary after modification: {'name': 'Alice', 'age': 40, 'city': 'New York', 'profession': 'Doctor'}

    City: New York

"""


# Initialize a dictionary with three key-value pairs representing personal information
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

# Print the original dictionary to show its initial state
print(f'Original Dictionary: {my_dict}')

# Add a new key-value pair 'profession':'Doctor' to the dictionary
my_dict["profession"] = 'Doctor'

# Print the updated dictionary showing the newly added key-value pair
print(f"Updated dictionary after adding 'profession': {my_dict}")

# Modify the value of the existing 'age' key from 35 to 40
my_dict['age'] = 40

# Print the modified dictionary showing the updated age value
print(f"Updated dictionary after modification: {my_dict}")

# Access and print the value associated with the 'city' key
print(f"City: {my_dict['city']}")