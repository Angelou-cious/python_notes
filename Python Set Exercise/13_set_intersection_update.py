"""
    Exercise 13: Set Intersection Update

    Write a code to remove items from set1 that are not present in set2.
"""

# Initialize the first set with a collection of integer values.
set1 = {10, 20, 30, 40, 50}
# Initialize the second set with another collection of integer values.
set2 = {30, 40, 50, 60, 70}

# The intersection_update() method modifies set1 in-place.
# It removes any items from set1 that are not present in set2.
# After this operation, set1 will only contain elements that are common to both sets.
set1.intersection_update(set2)
# Print the modified set1 to display the result of the intersection update.
print(set1)
