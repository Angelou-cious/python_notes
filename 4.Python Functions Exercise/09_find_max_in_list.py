def largest(lst1):                # Function that finds the largest number in a list
    
    # use not slice e.g [0::]
    current = lst1[0]             # Initialize current with first element of list
    
    for element in lst1:          # Loop through each element in the list
        if element > current:      # If current element is greater than stored value
            current = element      # Update current to store the larger value

    return current                # Return the largest number found

x = [4, 6, 8, 24, 12, 2]         # Create a test list with some numbers

print(largest(x))                 # Call the largest() function and print result
