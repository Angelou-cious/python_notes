# We start by setting factorial to 1 (this will store our final result)
factorial = 1

# We want to calculate factorial of 5 (n = 5)
n = 5

# This loop runs from 1 to n (5)
# Each time through the loop, we multiply factorial by the current number
for fact in range(1, n + 1):
    factorial = factorial * fact   # Example: 1*1, then 1*2, then 2*3, then 6*4, then 24*5
    
# Finally, print the result (which will be 5! = 5*4*3*2*1 = 120)
print(factorial)