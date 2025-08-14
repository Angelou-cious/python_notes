"""
    Exercise 8: Swap two tuples in Python
"""

# Create the first tuple, tuple1, with two integer elements.
tuple1 = (11, 22)
# Create the second tuple, tuple2, with two integer elements.
tuple2 = (99, 88)

# This line performs the tuple swapping.
# It simultaneously assigns the value of tuple2 to tuple1 and the value of tuple1 to tuple2.
tuple1, tuple2 = tuple2, tuple1

# Print the swapped tuples to the console using an f-string for formatted output.
print(f'Tuple1: {tuple1}, Tuple2: {tuple2}')
