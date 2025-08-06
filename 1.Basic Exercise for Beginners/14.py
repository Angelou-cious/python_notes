def myfunc(num):

    for item in range(num, 0, -1):
        for j in range(item):
            print('*', end=' ')
        print('')

myfunc(5)