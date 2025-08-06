# store the input
number = int(input(f'Enter number here: '))

# create variable to store all numbers
results = 0

# run loop n times
# stop: number + 1 (because range never include stop number in result)
for num in range(1, number + 1):

    # add the current iteration to the results variable
    results = num + results

print(f'sum is {results}')