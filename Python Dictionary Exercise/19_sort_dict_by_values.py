"""
    Exercise 19: Sort Dictionary by Values

    Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
"""

from collections import OrderedDict  # Import OrderedDict to maintain insertion order


def sort_dict_by_values(dict1):  # Define function to sort dictionary by values
    

    ordered_dict = OrderedDict(sorted(dict1.items(), key=lambda x : x[1]))  # Sort dict items by value (x[1]) and create OrderedDict

    return ordered_dict  # Return the sorted OrderedDict

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}  # Create sample dictionary with name-score pairs



print(f'Original dictionary: {my_dict}')  # Display the original unsorted dictionary

print()  # Print empty line for better formatting
print(f'Sorted by values (as OrderedDict):')  # Print header for sorted output
print(sort_dict_by_values(my_dict))  # Call function and print the sorted dictionary

