"""
    Exercise 14: Find Common Elements in Two Lists

    list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], find the common elements using sets.
"""

# Define the first list of numbers.
list1 = [10, 20, 30, 40]
# Define the second list of numbers.
list2 = [30, 40, 50, 60]

# Convert the first list to a set to perform set operations.
set1 = set(list1)
# Convert the second list to a set to perform set operations.
set2 = set(list2)

# Find the intersection of the two sets, which contains elements common to both.
x = set1.intersection(set2)

# Print the set of common elements.
print(x)
