# Function that finds even numbers in a list using filter and lambda
def get_even(lst): # Defines a function named 'get_even' that takes a list 'lst' as input.
    # Uses filter() with a lambda function to keep only even numbers
    # lambda element: element % 2 == 0 checks if each number is divisible by 2
    # filter() applies the lambda to each element and keeps only True results
    # list() converts the filter object to a list
    even_list = list(filter(lambda element: element % 2 == 0, lst)) # This line uses the 'filter' function to create a new list 'even_list'. The lambda function 'lambda element: element % 2 == 0' checks if each 'element' in the input list 'lst' is even. 'filter' returns an iterator with only the elements for which the lambda function is true. 'list()' converts this iterator to a list.

    # Print the resulting list of even numbers
    print(even_list) # This line prints the 'even_list' to the console.


# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # This line creates a list of integers from 1 to 10.

# Call the get_even function with our numbers list
get_even(numbers)  # Will print [2, 4, 6, 8, 10] # This line calls the 'get_even' function and passes the 'numbers' list as an argument, which will then print the even numbers from the list.
