def myfunc(numbers):
    print(f"Given list is {numbers}")
    print(f"Divisible by 5")

    for i in numbers:
        if i % 5 == 0:
            print(i)

myfunc([10, 20, 33, 46, 55])

