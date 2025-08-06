# Define a function that accepts any number of keyword arguments using **kwargs
def print_info(**kwargs):

    # Loop through each key-value pair in the kwargs dictionary
    for key, value in kwargs.items():
        # Print each key-value pair using f-string formatting
        print(f'{key} is {value}')


# Call the function with three keyword arguments:
# name='Angelou', age=25, and status='Unemployed'
print_info(name = 'Angelou', age= 25, status = 'Unemployed')
