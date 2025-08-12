"""
    Exercise 11: Create a dictionary by extracting the keys from a given dictionary

    Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
"""
# my code
def mod_dict(dict1, list1):  # Define function to extract specific keys from dictionary
    new_dict = {}  # Initialize empty dictionary to store extracted key-value pairs

    for item in list1:  # Iterate through each key in the list of keys to extract
        new_dict[item] = dict1[item]  # Copy key-value pair from original dictionary to new dictionary
    return new_dict  # Return the new dictionary with extracted keys

sample_dict = {  # Create sample dictionary with employee information
    "name": "Kelly",  # Employee name
    "age": 25,  # Employee age
    "salary": 8000,  # Employee salary
    "city": "New york"}  # Employee city

# Keys to extract
keys = ["name", "salary"]  # List of keys to extract from the sample dictionary

res = mod_dict(sample_dict, keys)  # Call function to extract specified keys

print(res)  # Print the resulting dictionary with extracted key-value pairs


# best practice
sampleDict = {  # Create sample dictionary with employee information
  "name": "Kelly",  # Employee name
  "age":25,  # Employee age
  "salary": 8000,  # Employee salary
  "city": "New york" }  # Employee city

keys = ["name", "salary"]  # List of keys to extract from the sample dictionary

newDict = {k: sampleDict[k] for k in keys}  # Dictionary comprehension to extract specified keys
print(newDict)  # Print the resulting dictionary with extracted key-value pairs