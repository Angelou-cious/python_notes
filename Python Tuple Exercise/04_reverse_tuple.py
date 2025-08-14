"""
    Exercise 4: Reverse the tuple
    This exercise demonstrates how to reverse a tuple using slicing
"""

# Create a tuple with 5 integer elements in ascending order
# Tuples are immutable sequences that can store multiple items
tuple1 = (10, 20, 30, 40, 50)

# Use slicing with step -1 to reverse the tuple
# [::-1] means: start from end, go to beginning, with step of -1
# This creates a new tuple with elements in reverse order
reversed_tuple = tuple1[::-1]

# Print the reversed tuple to display the result
# This will output: (50, 40, 30, 20, 10)
print(reversed_tuple)
