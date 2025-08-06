def factorial(number):                    # Define a function that calculates factorial of a given number
    if number == 0 or number == 1:        # Base case: if number is 0 or 1
        return 1                          # Return 1 as factorial of 0 or 1 is 1
    else:                                 # For all other numbers
        x = number * (factorial(number - 1))  # Multiply current number with factorial of (number-1)
        print(x)                          # Print the intermediate factorial result
        return x                          # Return the calculated factorial value

factorial(10)                             # Call the factorial function with input 10
