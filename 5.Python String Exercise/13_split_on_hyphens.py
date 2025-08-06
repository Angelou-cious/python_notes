# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# using split() method

def split_string(str): # Define a function that takes a string as a parameter

    words = str.split('-') # Split the string by the hyphen delimiter

    for word in words: # Loop through the list of words created by split()
        print(word) # Print each word on a new line

str1 = "Emma-is-a-data-scientist" # Define the input string

split_string(str1) # Call the function with the input string
