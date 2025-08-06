def myfunc(base, exp):

    results = 1

    if exp >= 0:
        for i in range(exp):
            results *= base
        print(f'{base} raise to the power of {exp} is: {results}')
        return results

print(myfunc(5, 4))