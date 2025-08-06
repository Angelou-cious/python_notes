def middle_threes_string(string):    # Define a function that takes a string parameter

    middle_string = int(len(string) / 2)    # Calculate the middle position by dividing string length by 2

    middle_char = string[middle_string - 1:middle_string + 2]    # Extract 3 chars: one before middle, middle, and one after

    print(middle_char)    # Print the extracted middle three characters

str1 = "JhonDipPeta"    # First test string

middle_threes_string(str1)    # Call function with first test string

str2 = "JaSonAy"    # Second test string

middle_threes_string(str2)    # Call function with second test string
