"""
    Clear Dictionary

    Clear all key-value pairs from a given dictionary and print it.
"""

# Initialize a dictionary with three key-value pairs containing personal information
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

# Use the clear() method to remove all key-value pairs from the dictionary
# This operation empties the dictionary completely, leaving it with zero items
# The original dictionary object still exists but now contains no elements
my_dict.clear()

# Print the dictionary after clearing to show it is now empty
# The output will be {} demonstrating that all elements have been removed
print(my_dict)