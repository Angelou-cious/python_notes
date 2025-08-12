"""
    Merge two Python dictionaries into one

    Write a code to merge two dictionaries into a new dictionary and print it.

"""

# Initialize the first dictionary with three key-value pairs
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Initialize the second dictionary with three key-value pairs
# Note: 'Thirty' key appears in both dictionaries with the same value
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Merge the two dictionaries using the pipe operator (|)
# This combines key-value pairs from both dictionaries
# For overlapping keys, values from the second dictionary (dict2) take precedence
dict3 = dict1 | dict2

# Sort the merged dictionary by its values in descending order
# Step 1: dict3.items() returns a list of (key, value) tuples
# Step 2: sorted() sorts these tuples using the lambda function as key
#   - lambda x: x[1] extracts the value from each tuple for sorting
#   - reverse=True sorts in descending order (highest value first)
# Step 3: dict() converts the sorted list of tuples back into a dictionary
# Note: Since Python 3.7+, dictionaries preserve insertion order
dict3 = dict(sorted(dict3.items(), key= lambda x : x[1], reverse= True))

# Print the final sorted dictionary showing items ordered by value descending
# Format: {'Fifty':50, 'Fourty':40, 'Thirty':30, 'Twenty':20, 'Ten':10}
print(dict3)