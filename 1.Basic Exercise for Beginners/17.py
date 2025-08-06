def myfunc():

    num1 = 0
    num2 = 1
    results = 0


    for i in range(15):
        print(f'{num1}', end=' ')
        results = num1 + num2

        num1 = num2

        num2 = results
        # return results

print(myfunc())