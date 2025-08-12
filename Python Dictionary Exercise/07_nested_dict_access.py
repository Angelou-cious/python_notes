"""
    Access Nested Dictionary

    Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.

"""

def get_age(data={'person': {'name': 'Alice', 'age': 30}}):
    # Access nested dictionary: get 'age' from 'person' dictionary
    age = data['person']['age']
    
    # Access nested dictionary: get 'name' from 'person' dictionary
    name = data['person']['name']
    
    # Return both values as a set (unordered collection)
    return {name, age}

# Create sample data dictionary with nested structure
data = {'person': {'name': 'Alice', 'age': 30}}

# Call function and unpack returned set into two variables
# WARNING: Sets are unordered so a and b may swap positions!
# - a could be name OR age
# - b could be age OR name
a, b = get_age(data)

# Print formatted string using unpacked variables
# Note: Output may be inconsistent due to set ordering
print(f"{a}'s age is: {b}")