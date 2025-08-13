"""
    Find the union of set1 and set2. Write a Python program to return a new set with unique items from both sets by removing duplicates.

    Expected Output:

        {70, 40, 10, 50, 20, 60, 30}
"""

# Create the first set named set1 with integer elements.
set1 = {10, 20, 30, 40, 50}

# Create the second set named set2 with integer elements.
set2 = {30, 40, 50, 60, 70}

# Perform the union operation on set1 and set2 using the '|' operator.
# The result is a new set containing all unique elements from both sets.
set3 = set1 | set2

# Print the resulting set, which is the union of set1 and set2.
print(set3)
