def high_low(num):
    
    # Convert the absolute value of the number to a string to iterate over digits
    s_num = str(abs(num))
    
    # Initialize small to 9 and large to 0
    # This handles the case where the smallest digit is never less than the initial value
    small = 9
    large = 0
    
    for digit_char in s_num:
        digit = int(digit_char)
        if digit > large:
            large = digit
        if digit < small:
            small = digit
            
    return (large, small)

num1 = 9876543210
num2 = -5082

largest, smallest = high_low(num1)
print(f'Largest digit in {num1}: {largest}')
print(f'Smallest digit in {num1}: {smallest}')
print()
largest, smallest = high_low(num2)
print(f'Largest digit in {num2}: {largest}')
print(f'Smallest digit in {num2}: {smallest}')
