def comparison(n):


    last = n[-1]

    if n[0] == last:
        return True
    else:
        return False
    

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

print(comparison(numbers_x))
print(comparison(numbers_y))