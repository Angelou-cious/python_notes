"""
    Exercise 11: Set Intersection Check

    Write a code to check if two sets have any elements in common. If yes, display the common elements
"""

set1 = {10, 20, 30, 40, 50}  # Define the first set with integer values.
set2 = {60, 70, 80, 90, 10}  # Define the second set with integer values.

set3 = set1.intersection(set2)  # Find the intersection of set1 and set2, which are the elements present in both sets.

print(set3)  # Print the resulting set containing the common elements.
