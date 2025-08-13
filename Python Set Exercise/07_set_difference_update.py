"""
    Exercise 7: Set Difference Update

    Given two Python sets, write a program to update the first set with only the items that are unique to it (i.e., not present in the second set).
"""

# Create the first set named set1 with integer elements.
set1 = {10, 20, 30}

# Create the second set named set2 with integer elements.
set2 = {20, 40, 50}

# Calculate the difference between set1 and set2.
# The difference operation returns a new set containing elements that are in set1 but not in set2.
set3 = set1.difference(set2)

# Print the resulting set3, which contains only the unique elements from set1.
print(set3)
