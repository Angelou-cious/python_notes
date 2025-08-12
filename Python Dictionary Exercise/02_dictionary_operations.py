"""
    Exercise 2: Perform dictionary operations

    Perform following operations on given dictionary

    Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
    Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
    Check if Key Exists in the dictionary

"""

# Initialize a dictionary with four key-value pairs including personal information and profession
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

# Print the original dictionary showing all key-value pairs including profession
print(f"Original dictionary: {my_dict}")

# Remove the 'profession' key-value pair from the dictionary using del statement
del my_dict['profession']

# Print the updated dictionary showing that profession has been removed
print(f"Updated dictionary after removing 'profession': {my_dict}")

# Print a header for the key-value pair listing (using incorrect method)
print("Printing all key-value pairs:")

# Iterate through dictionary keys but incorrectly print static text instead of values
# This demonstrates a common mistake - accessing keys without their corresponding values
for key in my_dict:
    print(f"{key} : value")  # Incorrect: should use my_dict[key] to get the value

# Print a header for the proper key-value pair listing using items()
print("Printing all key-value pairs:")

# Correctly iterate through all key-value pairs using items() method
# This properly accesses both the key and its corresponding value
for key, value in my_dict.items():
    print(f"{key} : {value}")

# Check if 'age' key exists in the dictionary using membership operator
# Prints True if key exists, False otherwise
print(f"Does 'age' exist? {'age' in my_dict}")

