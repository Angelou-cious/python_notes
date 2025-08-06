# Function that takes a list as parameter
def lambda_map(lst):
    
    # Uses map() to apply lambda function (x*2) to each element in lst
    # Lambda creates an anonymous function that doubles each number
    # List() converts the map object to a list
    res = list(map(lambda x : x *2 , lst))

    # Returns the resulting list of doubled numbers
    return res

# Creates a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# Calls lambda_map function with 'numbers' list and prints the result
# Using f-string for formatted output
print(f'The doubled numbers are: {lambda_map(numbers)}')