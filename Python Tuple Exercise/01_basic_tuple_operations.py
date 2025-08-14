"""
    Exercise 1: Perform Basic Tuple Operations

    Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.

    Access Elements: Access and print the third element of my_tuple.

    Tuple Length: Find and print the length of my_tuple.

    My tuple: (1, 2, 3, 4, 5)
    The third element of my_tuple: 3
    The length of my_tuple: 5
"""

# Create a tuple named 'my_tuple' using parentheses () to define an immutable sequence
# The tuple contains five integer elements: 1, 2, 3, 4, and 5
# Tuples are ordered collections that cannot be modified after creation (immutable)
my_tuple = (1,2,3,4,5)

# Use an f-string (formatted string literal) to display the entire tuple
# The f-string allows embedding expressions inside {} within the string
# This prints the complete tuple with its parentheses and comma-separated values
print(f'My tuple: {my_tuple}')

# Access the third element using index [2] (zero-based indexing: 0, 1, 2...)
# In Python, indexing starts at 0, so index 2 refers to the third element
# Use f-string formatting to display both descriptive text and the accessed value
print(f'The third element of my_tuple: {my_tuple[2]}')

# Use the built-in len() function to calculate the number of elements in the tuple
# len() returns an integer representing the total count of items in the sequence
# Display the result using f-string formatting for clear, readable output
print(f'The length of my_tuple: {len(my_tuple)}')
