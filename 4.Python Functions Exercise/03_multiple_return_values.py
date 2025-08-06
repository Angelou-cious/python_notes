def calculation(num1, num2):    # Define a function 'calculation' that takes two parameters num1 and num2

    addition = num1 + num2      # Calculate the sum of num1 and num2, store in 'addition' variable
    subtraction = num1 - num2   # Calculate num1 minus num2, store in 'subtraction' variable

    return addition, subtraction # Return both values as a tuple

res = calculation(40, 10)       # Call the function with arguments 40 and 10, store result in 'res'
print(res)                      # Print the tuple containing both addition and subtraction results
