
# loop the rows start from 5 to 1
for row in range(5, 0, -1):

    # loop the column from row to 0 in reverse
    for column in range(row, 0, -1):
        # Print current column number with a space
        # In each iteration, this prints the value of 'column' followed by a space
        # For example, when row=5, it prints: 5 4 3 2 1
        # When row=4, it prints: 4 3 2 1
        # And so on, creating a descending pattern
        print(column, end=" ")
    print()