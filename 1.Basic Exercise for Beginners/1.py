def myfun(num1, num2):
    
    product = num1 * num2

    if product <= 1000:
        return product

    else:
        return num1 + num2


print(myfun(20,30))
print(myfun(40,30))
