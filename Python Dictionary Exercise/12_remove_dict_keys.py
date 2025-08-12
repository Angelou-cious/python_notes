"""
    Exercise 12: Delete a list of keys from a dictionary
"""

def rem_dict(dict1, list1):  # Define function to remove keys from dictionary
 
    for item in list1:  # Iterate through each key to be removed

        dict1.pop(item)  # Remove the key-value pair from dictionary
        
        dict1 = dict(sorted(dict1.items(), key=lambda x: x[0],reverse=True))  # Sort dictionary by keys in reverse alphabetical order
        
    return dict1  # Return the modified dictionary


sample_dict = {  # Create sample dictionary with employee information
    "name": "Kelly",  # Employee name
    "age": 25,  # Employee age
    "salary": 8000,  # Employee salary
    "city": "New york"  # Employee city
}

# Keys to remove
keys = ["name", "salary"]  # List of keys to remove from the dictionary

x = rem_dict(sample_dict, keys)  # Call function to remove specified keys

print(x)  # Print the resulting dictionary after key removal