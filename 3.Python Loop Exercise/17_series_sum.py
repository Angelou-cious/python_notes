# This script calculates the sum of a series where each term is a repetition of a given digit.
# For example, if the digit is 2 and the number of terms is 5, the series is 2 + 22 + 222 + 2222 + 22222.

# The digit to be repeated in the series.
num = 2
# The number of terms in the series.
terms = 5
# This variable will store the cumulative sum of the series.
sum_of_series = 0
# This variable holds the value of the current term in each iteration.
current_term = 0

# The loop iterates 'terms' times to generate each term of the series.
# In each iteration, the current term is updated to form the next number in the sequence
# (e.g., 2 becomes 22, 22 becomes 222), and this new term is added to the total sum.
for i in range(terms):
    current_term = current_term * 10 + num
    sum_of_series += current_term
    print(current_term)

# Finally, the total sum of the series is printed.
print(sum_of_series)
