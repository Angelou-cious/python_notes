# Function that takes a list of numbers as input
def reversed_lists(numbers):
    
    # Use built-in reversed() function to create an iterator of the list in reverse order
    # Note: reversed() doesn't modify the original list, it creates a new iterator
    reversed_lists = reversed(numbers)

    # Iterate through each number in the reversed iterator
    # The loop will print numbers from last to first
    for number in reversed_lists:
        print(number)

# Create a sample list with 5 numbers
list1 = [10, 20, 30, 40, 50]

# Call the function with list1 as argument
# This will print: 50, 40, 30, 20, 10 (each on a new line)
reversed_lists(list1)