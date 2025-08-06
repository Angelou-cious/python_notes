def count(str):    # Function that takes a string parameter and counts characters, digits and symbols
    
    # Initialize counters for tracking different character types
    chars = 0      # Counter for alphabetic characters
    digits = 0     # Counter for numeric digits
    symbols = 0    # Counter for special symbols/characters

    for char in str:           # Iterate through each character in the input string
        if char.isalpha():     # Check if character is a letter (a-z, A-Z)
            chars += 1         # Increment character counter
        elif char.isdigit():   # Check if character is a number (0-9)
            digits += 1        # Increment digit counter
        else:                  # If character is neither letter nor digit
            symbols += 1       # Increment symbol counter
    return (chars, digits, symbols)  # Return all three counters as a tuple

str1 = "P@#yn26at^&i5ve"      # Test string containing mix of chars, digits and symbols

chars, digits, symbols = count(str1)  # Call count function and unpack returned tuple into variables

print(f'Total counts of chars, digits, and symbols')  # Print header for results
print(f'Chars = {chars}')      # Display count of alphabetic characters
print(f'Digits = {digits}')    # Display count of numeric digits
print(f'Symbols = {symbols}')  # Display count of special symbols
