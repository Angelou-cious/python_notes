"""
    Exercise 9: Copy Specific Elements From Tuple

    Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
"""

# Defines a tuple named tuple1 containing six integer elements.
tuple1 = (11, 22, 33, 44, 55, 66)

# Creates a new tuple named new_tuple by slicing tuple1.
# The slice [3:5] extracts elements from index 3 up to (but not including) index 5.
# This corresponds to the elements 44 and 55.
new_tuple = tuple1[3:5]

# Prints the contents of new_tuple to the console.
print(new_tuple)
