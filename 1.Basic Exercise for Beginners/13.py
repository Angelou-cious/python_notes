def myfunc():

    for i in range(1,11):
        for j in range(1,11):
            print(i * j, end=" ")
        print('\n')

myfunc()




def myfunc2(list):

    for i in list:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)

myfunc2([12, 75, 150, 180, 145, 525, 50])


def count_digits(number):

    counter = 0

    while number != 0:
        counter += 1
        number = number // 10   

    print(counter)


count_digits(75869)


