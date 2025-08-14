"""
    Exercise 3: Slicing Tuples

    Slice below tuple to get elements from the 4th to the 7th position.
"""

# Create a tuple containing integers from 1 to 10
# Tuples are immutable sequences that store multiple items in a single variable
# The parentheses () define the tuple, and commas separate the elements
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slice the tuple to extract elements from index 3 to 6 (4th to 7th position)
# Python uses zero-based indexing, so index 3 = 4th position, index 6 = 7th position
# Syntax: tuple[start:stop:step] where start is inclusive, stop is exclusive
# numbers[3:7:] means: start at index 3, stop before index 7, use default step of 1
# The extra colon at the end is optional when using default step
sliced_tuples = numbers[3:7:]

# Print the sliced tuple to display the result
# This will output: (4, 5, 6, 7) - elements at positions 4, 5, 6, and 7
print(sliced_tuples)
