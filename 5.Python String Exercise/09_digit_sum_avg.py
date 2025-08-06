# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

def sum_and_av(str):    # Define a function that takes a string as a parameter

    res = 0              # Initialize a variable to store the sum of digits
    count = 0            # Initialize a counter for the number of digits found

    for item in str:     # Loop through each character in the input string
        if item.isdigit(): # Check if the character is a digit
            item = int(item) # Convert the digit character to an integer
            res = item + res # Add the integer to the running sum
            count += 1       # Increment the digit counter
    av = res / count     # Calculate the average of the digits
    return res, av       # Return both the sum and the average


str1 = "PYnative29@#8496"  # Define the input string containing letters, digits, and symbols

sum, av = sum_and_av(str1) # Call the function and unpack the returned tuple into two variables

print(f'Sum is: {sum} Average is  {av:.2f}') # Print the final sum and the average formatted to two decimal places
