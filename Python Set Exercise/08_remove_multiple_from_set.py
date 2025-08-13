"""
    Exercise 8: Remove Items From Set Simultaneously

    Write a Python program to remove items 10, 20, 30 from the following set at once.
"""

# Create a set named set1 with initial values.
set1 = {10, 20, 30, 40, 50}

# Use the difference_update() method to remove multiple items (10, 20, 30) from the set.
# This method modifies the set in place.
set1.difference_update({10, 20, 30})

# Print the updated set to the console.
print(set1)
