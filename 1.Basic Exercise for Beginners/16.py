def is_palindrome_while_loop(num):

    original_num = num
    reversed_num = 0
    

    while num > 0:

       remainder = num % 10

       reversed_num = (reversed_num * 10) + remainder

       num //= 10 # floor division to 10

    return reversed_num == original_num
    
print(is_palindrome_while_loop(121))
print(is_palindrome_while_loop(12321))
print(is_palindrome_while_loop(5005))
print(is_palindrome_while_loop(5000))

    