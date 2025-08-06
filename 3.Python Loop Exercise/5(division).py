def division(numbers):

    # new_lists = []

    # iterate each item of a list
    for i in numbers:
        if i > 500:
            break
        elif i > 150:
            continue

        # check if number is divisible by 5
        elif i % 5 == 0:
            print(i)
            # new_lists.append(i)
    # return new_lists

numbers = [12, 75, 150, 180, 145, 525, 50]

print(division(numbers))
print()
division(numbers)