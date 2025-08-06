def high_low(num):
    # Convert negative numbers to positive using absolute value
    num = abs(num)

    # Special case: if number is 0, return 0 for both high and low
    if num == 0:
        return 0,0
    
    # Get the rightmost digit of the number
    first_digit = num % 10

    # Initialize both high and low with the first digit
    high = first_digit
    low = first_digit

    # Continue loop until all digits are processed (num becomes 0)
    while num != 0:
        # Get the rightmost digit using modulo
        remainder = num % 10

        # Update high if current digit is larger
        if remainder > high:
            high = remainder
        # Update low if current digit is smaller
        if remainder < low:
            low = remainder
        
        # Remove the rightmost digit by integer division
        num = num // 10

    # Return the highest and lowest digits found
    return high, low


# Test case 1: Negative number
num2 = -5082
high, low = high_low(num2)
# Display results for negative number
print(f'Largest digit in {num2}: {high}')
print(f'Lowest digit in {num2}: {low}', end="\n")

print()

# Test case 2: Positive number with all digits 0-9
num1 = 9876543210
x, y = high_low(num1)
# Display results for positive number
print(f'Largest digit in {num1}: {x}')
print(f'Lowest digit in {num1}: {y}')