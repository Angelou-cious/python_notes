# Define a function named 'is_balance' that takes two string arguments, s1 and s2.
def is_balance(s1, s2):
    # Initialize a boolean variable 'flag' to True. This will be used to track if all characters in s1 are present in s2.
    flag = True
    # Start a for loop that iterates through each character in the string s1.
    for char in s1:
        # Check if the current character 'char' is present in the string s2.
        if char in s2:
            # If the character is found in s2, continue to the next iteration of the loop.
            continue
        else:
            # If the character is not found in s2, it means s1 is not a balanced string with respect to s2.
            # So, the function immediately returns False.
            return False
    # If the loop completes without finding any character in s1 that is not in s2, it means s1 is balanced.
    # The function returns the initial value of 'flag', which is True.
    return flag

# Assign the string "Yn" to the variable s1.
s1 = "Yn"
# Assign the string "PYnative" to the variable s2.
s2 = "PYnative"
# Call the 'is_balance' function with s1 and s2 as arguments and store the returned boolean value in s3.
s3 = is_balance(s1,s2)
# Print the value of s3 to the console. In this case, it will be True because both 'Y' and 'n' are in "PYnative".
print(s3)

# Assign the string "Ynf" to the variable s1.
s1 = "Ynf"
# Assign the string "PYnative" to the variable s2.
s2 = "PYnative"
# Call the 'is_balance' function with the new s1 and s2.
s3 = is_balance(s1,s2)
# Print the value of s3. It will be False because 'f' is not in "PYnative".
print(s3)
