def alternate(num): # Defines a function named 'alternate' that takes one argument, 'num'.

    for i in range(1,6): # Starts a 'for' loop that iterates from 1 to 5 (not including 6).
        for _ in range(i): # Starts a nested 'for' loop that iterates 'i' times.
            print(num, end=" ") # Prints the current value of 'num' followed by a space.
            num += 1 # Increments the value of 'num' by 1.
        print() # Prints a new line after each row of numbers.


current = 1 # Initializes a variable 'current' with the value 1.
alternate(current) # Calls the 'alternate' function with 'current' as the argument.
