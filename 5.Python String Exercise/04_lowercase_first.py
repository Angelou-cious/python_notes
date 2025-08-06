def lower_case(str):                    # Function definition that takes a string parameter
    
    lower = []                         # Initialize empty list to store lowercase characters
    upper = []                         # Initialize empty list to store uppercase characters

    for char in str:                   # Loop through each character in the input string
        if char.islower():             # Check if current character is lowercase
            lower.append(char)          # If lowercase, add it to lower list
        else:
            upper.append(char)          # If uppercase, add it to upper list

    return ''.join(lower + upper)      # Combine both lists and convert back to string


str1 = "PyNaTive"                      # Test string input

print(lower_case(str1))                # Call function and print result
