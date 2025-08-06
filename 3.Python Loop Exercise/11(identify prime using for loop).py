# This function finds prime numbers between 'start' and 'end' (inclusive)
def is_prime(start, end):
    
    # Loop through each number in our range (from start to end)
    for number in range(start, end + 1):

        # We only check numbers greater than 2
        # (because 1 is not prime, and 2 is handled differently)
        if number > 2:

            # For each number, we'll check if it's divisible by anything
            # We try dividing it by all numbers from 2 up to (number-1)
            for i in range(2, number):

                # If the number is divisible by any value (remainder = 0),
                # then it's not prime, so we break the loop
                if number % i == 0:
                    break

            # The else clause runs if the for loop completes without breaking
            # This means no divisors were found, so the number is prime
            else:
                print(number)    


# Define the range of numbers we want to check
start = 25  # Starting number
end = 50    # Ending number

# Call the function with our start and end values
is_prime(start, end)