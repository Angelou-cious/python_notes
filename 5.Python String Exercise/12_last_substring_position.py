# Exercise 12: Find the last position of a given substring using rfind()

# Write a program to find the last position of a substring “Emma” in a given string.


def f_l_p(str, find): # Define a function that takes a main string and a substring to find
    
    occur = str.rfind(find) # Use the rfind() method to find the last occurrence of the substring

    return occur # Return the starting index of the last occurrence


str1 = "Emma is a data scientist who knows Python. Emma works at google." # Define the main string


print(f'Last occurrence of Emma starts at index {f_l_p(str1, "Emma")}') # Call the function and print the result in a formatted string
