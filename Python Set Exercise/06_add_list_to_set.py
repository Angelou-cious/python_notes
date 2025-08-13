"""
    Exercise 6: Add a list of Elements to a Set

    Given a Python list, write a program to add all of its elements into a given set.
"""

# Initialize a set named sample_set with three string elements.
sample_set = {"Yellow", "Orange", "Black"}
# Initialize a list named sample_list with three string elements.
sample_list = ["Blue", "Green", "Red"]

# The update() method is called on sample_set.
# It takes sample_list as an argument, iterating through the list and adding each element to the set.
# Sets automatically handle duplicates, so only new elements are added.
sample_set.update(sample_list)

# The print() function displays the final state of sample_set after the update.
print(sample_set)
