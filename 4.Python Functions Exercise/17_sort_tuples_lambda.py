# Function that takes a list of tuples as input
def sorted_tuples(lst):

    # Sort the list using sorted() function with lambda as key
    # lambda element: element[1] means sort based on second element (index 1) of each tuple
    # reverse=False means ascending order
    new_list = sorted(lst , key=lambda element : element[1], reverse=False)

    # Return the sorted list
    return new_list


# Sample data: list of tuples containing fruit names and numbers
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

# Call the sorted_tuples function with our data and store result in x
x = sorted_tuples(data)

# Print the result using f-string formatting
print(f'The sorted list of tuples based on the second element is: {x}')