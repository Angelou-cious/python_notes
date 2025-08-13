"""
    Exercise 9: Check Subset

    Check if set1 is a subset of set2. Write a code to return True if every element in the subset_set is also present in the main_set.
"""

# Create a set named subset_set with elements 10 and 20.
subset_set = {10, 20}

# Create a set named main_set with elements 10, 20, 30, and 40.
main_set = {10, 20, 30, 40}

# Check if subset_set is a subset of main_set using the issubset() method.
# The issubset() method returns True if all elements of subset_set are present in main_set, otherwise it returns False.
# In this case, since both 10 and 20 are in main_set, it will print True.
print(subset_set.issubset(main_set))
