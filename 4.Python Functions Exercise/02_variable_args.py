# Define a function that can accept any number of arguments using *args
def func1(*args):
    # *args allows the function to accept variable number of arguments as a tuple

    # Loop through each argument passed to the function
    for number in args:
        # Print each argument on a new line
        print(number)

# Call func1 with 2 arguments (integers)
func1(10, 20)

# Call func1 with 3 arguments (string, float, and boolean)
func1("hello", 3.14, True)

# Call func1 with 5 arguments (integers)
func1(1, 2, 3, 4, 5)

# Call func1 with no arguments (empty tuple)
func1()  # Calling with no arguments