"""
    Exercise 5: Access Nested Tuples

    Write a code to access and print value 20 from given nested tuple.
"""

# Create a nested tuple containing three elements:
# - Element 0: A string "Orange"
# - Element 1: A list [10, 20, 30] containing three integers
# - Element 2: A tuple (5, 15, 25) containing three integers
# This demonstrates that tuples can contain different data types including other collections
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# Access and print the value 20 from the nested structure using double indexing:
# tuple1[1] - Access the second element (index 1) of tuple1, which is the list [10, 20, 30]
# [1] - Access the second element (index 1) of that list, which is the integer 20
# This is called "chained indexing" or "nested indexing"
print(tuple1[1][1])
