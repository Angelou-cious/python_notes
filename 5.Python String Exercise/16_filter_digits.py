# Exercise 16: Removal all characters from a string except integers
# Define a function named get_digits that takes one argument, str1.
def get_digits(str1):

    # Split the input string into a list of words.
    str1_lists = str1.split()

    # Create an empty list to store the digits.
    new_string = []

    # Loop through each element in the list of words.
    for element in str1_lists:
        # Check if the element consists of digits only.
        if element.isdigit():
            # If it's a digit, add it to the new_string list.
            new_string.append(element)
        
    # Join the elements in the new_string list to form a single string.
    return ''.join(new_string)

# expected output: 2510
# Define the input string.
str1 = 'I am 25 years and 10 months old'

# Call the get_digits function with the input string and store the result in 'res'.
res = get_digits(str1)

# Print the expected output for reference.
print(f'expected output: 2510')

# Print the final string containing only digits.
print(f'New string with only digits: {res}')
