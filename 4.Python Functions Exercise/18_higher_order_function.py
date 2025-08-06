# Higher-order function that takes another function and two numbers as arguments
def apply_operation(func, x, y):

    # Executes the passed function with x and y as arguments
    res = func(x,y)

    # Returns the result of the operation
    return res

# Lambda function for addition - takes x and y and returns their sum
addition = lambda x,y : x + y

# Calls apply_operation with addition function and numbers 10, 5
sum = apply_operation(addition, 10, 5)

# Lambda function for subtraction - takes x and y and returns their difference
subtraction = lambda x,y : x - y

# Calls apply_operation with subtraction function and numbers 10, 5
difference = apply_operation(subtraction, 10, 5)

# Lambda function for multiplication - takes x and y and returns their product
multiplication = lambda x,y : x * y

# Calls apply_operation with multiplication function and numbers 10, 5
product = apply_operation(multiplication, 10, 5)

# Prints the result of addition operation using f-string
print(f'Result of addition: {sum}')

# Prints the result of subtraction operation using f-string
print(f'Result of subtraction: {difference}')

# Prints the result of multiplication operation using f-string
print(f'Result of multiplication: {product}')
