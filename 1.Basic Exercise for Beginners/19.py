def myfunc(num):
    
    if num < 2:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1): # only get the square root of the num + 1
            if  num % i == 0: # check if the number is divisible by i
                return False
        return True
        
n = 50
primes = []

for num in range(2, n + 1):
    if myfunc(num):
        primes.append(num)
print(f'All prime numbers from 1 to {n}: {primes}')


print(f'Alternate prime numbers from 1 to {n}:')

for i in range(0, len(primes), 2):
    print(primes[i], end=' ')