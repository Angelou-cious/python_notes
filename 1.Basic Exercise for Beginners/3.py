def myfunc(char):
    
    char = list(char)

    for i in char[::2]:
        print(i)
    
x = input("input: \n")
myfunc(x)
