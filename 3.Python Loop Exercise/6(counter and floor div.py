
def counter(number):

    # initialize counter to store the count of the loop
    counter = 0

    # add condition to run loop if number is not 0
    while number != 0:
        # add + 1 in every iteration
        counter += 1

        # remove last digit using floor division
        number = number // 10

    print(f"So the output should be |{counter}|")

number = 75869
counter(number)