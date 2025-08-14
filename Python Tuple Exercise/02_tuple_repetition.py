"""
    Exercise 2: Tuple Repetition

    Repeat a below tuple three times.
"""

# Create a tuple containing two string elements 'a' and 'b'
# Tuples are immutable sequences defined using parentheses ()
# This tuple has 2 elements at index 0 and 1
original_tuple = ('a', 'b')

# Use the repetition operator (*) to repeat the tuple 3 times
# The * operator creates a new tuple by concatenating the original tuple with itself
# This results in: ('a', 'b') + ('a', 'b') + ('a', 'b') = ('a', 'b', 'a', 'b', 'a', 'b')
# The new tuple will have 6 elements (2 original elements × 3 repetitions)
modified_tuple = original_tuple * 3

# Display the resulting tuple to the console
# This will output: ('a', 'b', 'a', 'b', 'a', 'b')
# The print() function converts the tuple to its string representation for display
print(modified_tuple)
