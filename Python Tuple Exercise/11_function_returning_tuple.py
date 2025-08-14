"""
    Exercise 11: Function Returning Tuple

    Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.
"""

def get_min_max(numbers):
    # This line creates a new list called 'num' that contains only the integer and float values from the input 'numbers' list.
    # It uses a list comprehension to iterate through each element in 'numbers'.
    # The 'isinstance()' function checks if an element is of type 'int' or 'float'.
    num = [num for num in numbers if isinstance(num,(int, float))]
    
    # This line checks if the 'num' list is empty.
    # If it is empty (meaning no numbers were found in the input), it returns a tuple with two 'None' values.
    if not num:
        return (None, None)
        
    # This line finds the minimum value in the 'num' list and assigns it to the 'least' variable.
    least = min(num)
    
    # This line finds the maximum value in the 'num' list and assigns it to the 'high' variable.
    high = max(num)
    
    # This line returns a tuple containing the minimum and maximum values.
    return (least, high)

# This line defines a list of numbers that will be used to test the 'get_min_max' function.
# It includes a mix of positive and negative integers, as well as a string to test the filtering logic.
my_numbers = [10, 5, 20, 2, 15, -12, "f"]

# This line calls the 'get_min_max' function with 'my_numbers' as the argument.
# The returned tuple (containing the minimum and maximum values) is stored in the 'min_max_values' variable.
min_max_values = get_min_max(my_numbers)

# This line prints the original list of numbers to the console.
# The 'f-string' formatting is used to embed the 'my_numbers' list directly into the string.
print(f"Original numbers: {my_numbers}")

# This line prints the minimum and maximum values found by the function.
# The 'f-string' formatting is used to embed the 'min_max_values' tuple directly into the string.
print(f"Minimum and maximum values: {min_max_values}")
