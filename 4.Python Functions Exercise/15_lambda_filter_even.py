# Function that finds even numbers in a list using filter and lambda
def get_even(lst):
    # Uses filter() with a lambda function to keep only even numbers
    # lambda element: element % 2 == 0 checks if each number is divisible by 2
    # filter() applies the lambda to each element and keeps only True results
    # list() converts the filter object to a list
    even_list = list(filter(lambda element: element % 2 == 0, lst))

    # Print the resulting list of even numbers
    print(even_list)


# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the get_even function with our numbers list
get_even(numbers)  # Will print [2, 4, 6, 8, 10]