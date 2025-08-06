

def sum(num):

    if num:
        res = num + sum(num - 1)
        print(res)
        return res
    else:
        return 0
    
print(sum(10))