# Initialize first two numbers of Fibonacci sequence
num1 = 0  # First number
num2 = 1  # Second number

# Loop 10 times to generate first 10 numbers of Fibonacci sequence
for fib in range(10):
    # Print current number (num1) followed by a space
    print(num1, end=' ')

    # Calculate next Fibonacci number by adding previous two numbers
    results = num1 + num2

    # Shift numbers: num1 becomes num2
    num1 = num2

    # num2 becomes the new calculated result
    num2 = results
