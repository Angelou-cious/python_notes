"""
    Exercise 13: Removing Duplicates from Tuple

    Write a code to create a new tuple with only unique elements.
"""

# Original tuple with duplicate elements
my_tuple = (1, 2, 2, 3, 4, 4, 5)

# Convert the tuple to a set to remove duplicates, then convert it back to a tuple
new_tuple = tuple(set(my_tuple))

# Print the original tuple
print(my_tuple)
# Print the new tuple with unique elements
print(new_tuple)
