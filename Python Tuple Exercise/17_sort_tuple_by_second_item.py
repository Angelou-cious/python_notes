"""
    Exercise 17: Sort a tuple of tuples by 2nd item
"""

# Define a tuple of tuples named tuple1. Each inner tuple contains a character and an integer.
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

# Sort the tuple 'tuple1' based on the second item (index 1) of each inner tuple.
# The `sorted()` function returns a new sorted list.
# The `key=lambda x: x[1]` argument tells sorted() to use the second element of each sub-tuple for sorting.
# The `tuple()` constructor is used to convert the resulting sorted list back into a tuple.
new_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))

# Print the newly sorted tuple to the console.
print(new_tuple)
