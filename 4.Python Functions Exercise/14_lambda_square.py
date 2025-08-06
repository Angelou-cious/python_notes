def get_square(num):                    # Defines a function that takes one parameter 'num'

    square = lambda num : num ** 2      # Creates a lambda function that squares its input
                                       # lambda is an anonymous function that takes 'num' and returns num^2

    print(square(num))                  # Calls the lambda function with the input parameter and prints the result

get_square(10)                         # Calls the get_square function with argument 10 (will print 100)