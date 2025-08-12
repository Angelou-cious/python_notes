
"""
    Exercise 18: Sort Dictionary by Keys

    Sort a dictionary by its keys and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).

    my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

    Original dictionary: {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

    Sorted by keys (as OrderedDict):
    OrderedDict([('apple', 3), ('banana', 2), ('cat', 4), ('zebra', 1)])

"""

from collections import OrderedDict  # Import OrderedDict to maintain insertion order for sorted dictionary

# my code
def sort_dict_by_keys(dict1):  # Define function to sort dictionary by keys manually


    list1 = sorted(dict1)  # Create sorted list of dictionary keys in alphabetical order

    new_dict = {}  # Initialize empty dictionary to store sorted key-value pairs

    for item in list1:  # Iterate through each key in the sorted key list

        new_dict[item] = dict1.get(item)  # Add key-value pair to new dictionary using get() method

       
    return new_dict  # Return the new dictionary with keys sorted alphabetically



my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}  # Create sample dictionary with unsorted keys

print(sort_dict_by_keys(my_dict))  # Call custom function to sort dictionary and print result

# other method
print(OrderedDict(sorted(my_dict.items())))  # Alternative method: use OrderedDict with sorted items() for more efficient sorting

# also mine
x = {}  # Initialize empty dictionary to store sorted key-value pairs
for key, value in sorted(my_dict.items()):  # Iterate through sorted key-value pairs from original dictionary
    x[key] = value  # Add each key-value pair to new dictionary in sorted order
print(x)  # Print the sorted dictionary