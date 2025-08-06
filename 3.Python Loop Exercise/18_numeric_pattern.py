# Outer loop for increasing part of the pattern
# i will be 1, 2, 3, 4, 5
for i in range(1, 6):
    # Inner loop to print asterisks in increasing order
    # When i is 1, j is 1, prints *
    # When i is 2, j is 2, 1, prints * *
    # When i is 3, j is 3, 2, 1, prints * * *
    for j in range(i, 0, -1):
        # Print an asterisk followed by a space
        print('*', end=" ")
    # Move to the next line after each row
    print()

# Outer loop for decreasing part of the pattern
# i will be 6, 5, 4, 3, 2, 1
for i in range(6, 0, -1):
    # Inner loop to print asterisks in decreasing order
    # When i is 6, j is 6, 5, 4, 3, 2, 1, prints * * * * * *
    # When i is 5, j is 5, 4, 3, 2, 1, prints * * * * *
    for j in range(i, 0, -1):
        # Print an asterisk followed by a space
        print('*', end=" ")
    # Move to the next line after each row
    print()
