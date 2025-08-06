global_var = 10                    # Initialize a global variable with value 10

def update_global():              # Define a function named update_global
    
    for i in range(5):           # Loop 5 times (i will be 0,1,2,3,4)
        global global_var        # Declare that we'll use the global variable inside the function
        
        global_var += 1         # Increment the global variable by 1
        print(global_var)       # Print the current value of the global variable

update_global()                 # Call the function to execute it
