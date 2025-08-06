def recursive(num):  # Define a function named 'recursive' that takes one argument 'num'

    if num:  # Check if 'num' is not zero (non-zero values are considered True)
        return num + recursive(num -1)  # If true, return 'num' plus the result of calling 'recursive' with 'num - 1'
    else:  # If 'num' is zero
        return 0  # Return 0 as the base case to stop recursion

print(recursive(10))  # Call the 'recursive' function with 10 and print the result
