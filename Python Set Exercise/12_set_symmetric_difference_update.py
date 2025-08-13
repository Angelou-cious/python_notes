"""
    Exercise 12: Set Symmetric Difference Update

    Write a program to update set1 by adding items from set2 that are not common to both sets.
"""

# Define the first set with integer values.
set1 = {10, 20, 30, 40, 50}

# Define the second set with integer values.
set2 = {30, 40, 50, 60, 70}

# Use the symmetric_difference_update() method to update set1.
# This method keeps only the elements that are unique to each set,
# effectively removing the common elements and adding the unique elements from set2 to set1.
set1.symmetric_difference_update(set2)

# Print the updated set1 to display the result.
# The output will be {10, 20, 60, 70}, which are the elements
# that were not common between the original set1 and set2.
print(set1)
