while True:
    try:
        input1 = int(input(f'1. Say Hello, 2. Calculate Square, 3. Exit: '))

        if input1 == 3:
            break # end the while loop

        elif input1 == 2:

            try:
                number = int(input(f'enter number: '))

                square = number ** 2

                print(f'the square of {number} is equal to {square}')
            except:
                print(f'invalid input')
            
        elif input1 == 1:
            print(f'Hello')

    except:
        print(f'Invalid Number')



