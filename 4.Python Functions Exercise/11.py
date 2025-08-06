def store_key_value(**k):    # Function that accepts arbitrary keyword arguments using **k

    dict = {}    # Initialize an empty dictionary to store key-value pairs

    for key, value in k.items():    # Loop through each key-value pair in the keyword arguments
        dict[key] = value    # Add each key-value pair to our dictionary

    return dict    # Return the populated dictionary
    
x = store_key_value(name = 'Angelou', age= 25, status = 'Unemployed')    # Call function with 3 keyword arguments and store result in x

for key, value in x.items():    # Loop through each key-value pair in the returned dictionary
    print(f'{key} is {value}')    # Print each key-value pair in a formatted string