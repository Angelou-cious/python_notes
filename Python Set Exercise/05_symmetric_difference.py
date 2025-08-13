"""
    Exercise 5: Symmetric Difference


    Find the symmetric difference of set1 and set2. Write a code to returns a new set containing elements that are unique to either set1 or set2, but not in both. It’s like finding the union and then removing the intersection.
"""

# Create the first set of numbers.
set1 = {10, 20, 30, 40, 50}
# Create the second set of numbers.
set2 = {30, 40, 50, 60, 70}

# Find the symmetric difference of the two sets using the '^' operator.
# This creates a new set containing elements that are in either set1 or set2, but not in both.
set3 = set1 ^ set2

# Print the resulting set which contains the symmetric difference.
print(set3)
