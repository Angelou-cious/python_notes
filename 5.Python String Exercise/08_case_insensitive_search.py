
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

def find_string(str):    # Define a function that takes a string as a parameter

    str = str.lower()    # Convert the input string to lowercase for case-insensitive comparison

    char = "USA"         # Define the substring to search for
    char = char.lower()  # Convert the substring to lowercase as well

    res = str.count(char) # Count the occurrences of the lowercase substring in the lowercase main string

    return res          # Print the final count

str1 = "Welcome to USA. usa awesome, isn't it?"  # Define the input string

print(f'The USA count is: {find_string(str1)}')  # Display the counts


