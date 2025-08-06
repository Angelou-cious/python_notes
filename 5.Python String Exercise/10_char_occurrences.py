# Exercise 10: Write a program to count occurrences of all characters within a string


def count_occurrence(strings): # Define a function that takes a string as a parameter

    dict = {} # Initialize an empty dictionary to store character counts

    for char in strings: # Loop through each character in the input string

        strings = str(strings) # This line is redundant as 'strings' is already a string

        count = strings.count(char) # Count the occurrences of the current character in the entire string

        dict[char] = count # Assign the count to the character key in the dictionary

    print(dict) # Print the final dictionary with character counts


str1 = "Apple" # Define the input string

count_occurrence(str1) # Call the function with the input string
