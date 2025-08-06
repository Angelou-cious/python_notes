def remove_chars(word, n):
    # write your code
    letters = list(word)

    x = letters[n:]
    return x


print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'



def get_evens(numbers):
    # Your code here
    list_nums = []
    
    for i in range(numbers):
        if i % 2 == 0:
            list_nums.append(i)
            
    return list_nums

print(get_evens(100))