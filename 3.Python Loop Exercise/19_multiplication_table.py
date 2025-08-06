# Outer loop to iterate through numbers 1 to 10 for the multiplication table
for number in range(1, 10 + 1):
    # Print the header for the current number's multiplication table
    print(f'multiplication table of: {number}')

    # Inner loop to multiply the current number by 1 to 10
    for i in range(1, 10 + 1):
        # Calculate the result of the multiplication
        res = i * number
        # Print the result without a newline, followed by a space
        print(f'{res}', end=" ")
    # Print a newline to separate the tables
    print()
