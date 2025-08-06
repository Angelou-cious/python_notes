# Store the name "Angelou" in variable str1
str1 = "Angelou"

# Calculate the middle index by dividing string length by 2 and converting to integer
length = int(len(str1)/2)

# Get first character (index 0) and convert to uppercase
first = str1[0].capitalize()

# Get middle character using calculated length index and convert to uppercase
middle_letter = str1[length].capitalize()

# Get last character (index -1) and convert to uppercase
last = str1[-1].capitalize()

# Print the three letters using f-string formatting
print(f'{first}{middle_letter}{last}')