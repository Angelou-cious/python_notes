def mix_string(s1,s2):    # Define a function that takes two strings as parameters

    s2_reversed = s2[::-1]        # Reverse the second string using string slicing

    new_string = []      # Initialize an empty list to store interleaved characters

    for a,b in zip(s1, s2_reversed):    # Loop through both strings simultaneously using zip
        new_string.append(a + b)    # Combine and append characters from both strings

    return ''.join(new_string)    # Join all characters into final string and return it

s1 = "Online Python Code Editor"           # First input string
s2 = "String characters balance Test"      # Second input string

s3 = mix_string(s1, s2)    # Call mix_string function and store result in s3

print(s3)    # Print the resulting interleaved string