"""
    Exercise 14: Rename key of a dictionary

    Write a program to rename a key city to a location in the following dictionary.

"""

sample_dict = {  # Create sample dictionary with employee information
  "name": "Kelly",  # Employee name
  "age":25,  # Employee age
  "salary": 8000,  # Employee salary
  "city": "New york"  # Employee city (key to be renamed)
}

sample_dict['location'] = sample_dict.pop('city')  # Rename 'city' key to 'location' by popping old key and assigning to new key

print(sample_dict)  # Print the dictionary with renamed key