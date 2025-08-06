def myfunc(num1):

    for i in range(1, num1 + 1): # start at 1, and ends in len num1 + 1 = 5
        for j in range(1, i + 1): # start at 1, and ends in len i + 1 = n
            print(f'{i}', end=' ')
        print('')

    for i in range(num1,0, -1): # reverse
        for j in range(1, i + 1): # start at 1, and ends in len i + 1 = n
            print(f'{j}', end=' ')
        print('')
myfunc(5)

