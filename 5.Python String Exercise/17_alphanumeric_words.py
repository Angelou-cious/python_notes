
# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.

# Define a function named get_alpha_num that takes one argument, str1.
def get_alpha_num(str1):

    # Split the input string into a list of words.
    str1_list = str1.split()

    # Create an empty list to store words containing both letters and numbers.
    new_list = []

    # Loop through each element (word) in the list of words.
    for element in str1_list:

        # Check if the element contains at least one letter AND at least one digit.
        if any(a.isalpha() for a in element) and any(b.isdigit() for b in element):
            # If the condition is true, add the element to new_list.
            new_list.append(element)

    # Return the list of alphanumeric words.
    return new_list


# Define the input string.
str1 = "Emma25 is Data scientist50 and AI Expert"


# Print the original input string.
print(f'The original input is: {str1}')

# Call the get_alpha_num function with the input string and store the result.
new_str1 = get_alpha_num(str1)

# Loop through the list of alphanumeric words and print each one on a new line.
for i in new_str1:
    print(i)
