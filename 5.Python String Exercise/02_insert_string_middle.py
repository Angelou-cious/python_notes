def append_middle(s1,s2):    # Define function that takes two string parameters

    middle = int(len(s1) / 2 )    # Calculate middle position by dividing length of s1 by 2 and converting to integer

    s3 = s1[:middle] + s2 + s1[middle:]    # Create new string by: taking first half of s1 + all of s2 + second half of s1

    print(s3)    # Print the resulting combined string


    print(f'{s1[:middle]}{s2}{s1[middle:]}')    # Alternative way using f-string: first half of s1 + s2 + second half of s1


# Test the function with example values
s1 = "Ault"    # First string to be split and combined
s2 = "Kelly"    # String to be inserted in the middle
append_middle(s1, s2)    # Call function with test strings - will print "AuKellylt"
