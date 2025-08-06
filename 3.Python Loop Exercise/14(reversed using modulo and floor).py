n = 76542 # initialize the number to be reversed
rev = 0 # initialize the variable to store the reversed number

while n > 0: # run the loop if its not zero

    remainder = n % 10 # get the last number using modulo 10

    rev = (rev * 10) + remainder # multiply the reversed num by 10 and add the remainder

    n = n // 10 # remove the last digit by using a floor division

print(rev) # print the reversed number