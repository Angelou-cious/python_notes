def calculate(a, b):                # Define outer function 'calculate' with two parameters a and b

    def sum(a,b):                   # Define nested function 'sum' inside calculate
        sum = a + b                 # Calculate the sum of parameters a and b
        
        return sum                  # Return the sum value from nested function

    res = sum(a, b) + 5            # Call nested function 'sum' and add 5 to its result
    
    return res                      # Return the final result from outer function

print(calculate(10, 10))            # Call calculate function with arguments 10,10 and print result
