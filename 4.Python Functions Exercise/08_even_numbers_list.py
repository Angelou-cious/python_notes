# Function that generates a list of even numbers between start and end parameters
def gen_list(start, end):

    # Initialize an empty list to store even numbers
    new_list = []

    # Loop through each number from start to end-1
    for element in range(start, end):
        # Check if the current number is even (divisible by 2 with no remainder)
        if element % 2 == 0:
            # If number is even, add it to our list
            new_list.append(element)

    # Return the list containing all even numbers
    return new_list

# Call the function with start=4 and end=30, store result in var
var = gen_list(4, 30)

# Print the list of even numbers
print(var)