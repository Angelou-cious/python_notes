# number of terms
num = 2
terms = 5

sum_of_term = 0 
current_term = 0

for i in range(terms):

    current_term = current_term * 10 + num
    sum_of_term += current_term

    print(current_term)
    
print()
print(sum_of_term)