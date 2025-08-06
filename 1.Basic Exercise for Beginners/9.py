def myfunc(num1):

    print(f"original number {num1}")

    num1 = str(num1)
    mirror = num1[::-1]

    if num1 == mirror:
        print(f"Yes. {num1} is a palindrome number")
    else:
        print(f"No. {num1} is not a palindrome number")

myfunc(12321)
