"""
    Exercise 20: Check if All Values are Unique

    Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.

    Dictionary: {'a': 1, 'b': 2, 'c': 3} -> All values unique? True
    Dictionary: {'x': 10, 'y': 20, 'z': 10} -> All values unique? False
    Dictionary: {} -> All values unique? True
"""

def check_unique_values(dict1):  # Define function to check if all dictionary values are unique

    dict1 = list(dict1.values())  # Extract all values from dictionary and convert to list

    new_dict = set(dict1)  # Convert list to set (removes duplicates automatically)

    if len(dict1) == len(new_dict):  # Compare original list length with set length
        return "Yes"  # If lengths are equal, all values were unique
    else:
        return "No"  # If lengths differ, there were duplicate values



dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique - test case 1
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated - test case 2
dict3 = {} # Empty dictionary (all values are vacuously unique) - test case 3

print(f"Dictionary: {dict1} is all unique? {check_unique_values(dict1)}")  # Test and display result for dict1
print(f"Dictionary: {dict2} is all unique? {check_unique_values(dict2)}")  # Test and display result for dict2
print(f"Dictionary: {dict3} is all unique? {check_unique_values(dict3)}")  # Test and display result for dict3