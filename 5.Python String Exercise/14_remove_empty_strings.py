# Exercise 14: Remove empty strings from a list of strings

def string_remove(list): # Define a function that takes a list of strings as a parameter

    print(f'Original list of string \n {list} \n') # Print the original list

    new_list = [] # Initialize an empty list to store non-empty strings

    for element in list: # Loop through each element in the input list
        if element == "" or element == None: # Check if the element is an empty string or None
            continue # Skip the current iteration if the condition is true
        else:
            new_list.append(element) # Append the element to the new list if it's not empty or None

    print(f'After removing empty string \n {new_list}') # Print the new list without empty strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""] # Define the input list of strings
string_remove(str_list) # Call the function with the input list
