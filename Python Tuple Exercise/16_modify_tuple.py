"""
    Exercise 16: Modify Tuple

    Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
"""

# Original tuple containing an integer, a list of integers, and two more integers.
tuple1 = (11, [22, 33], 44, 55)

# Access the list within the tuple (at index 1) and then the first element of that list (at index 0).
# Modify the value of this element to 222. This is possible because lists are mutable, even when nested inside an immutable tuple.
tuple1[1][0] = 222

# Print the modified tuple to display
print(tuple1)
