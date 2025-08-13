"""
    Exercise 10: Check Superset

    Check if main_set = {10, 20, 30, 40} is a superset of subset_set = {10, 20}.
"""

# Create the first set, which will be checked as a potential subset.
set1 = {10, 20}

# Create the second set, which will be checked to see if it is a superset of the first.
set2 = {10, 20, 30, 40}

# The issuperset() method returns True if all elements of set1 are present in set2.
# In this case, since {10, 20} is contained within {10, 20, 30, 40}, it will print True.
print(set2.issuperset(set1))
