# Exercise 7: Count Occurrences
# Count and print how many times 'Football' appears in list.


sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis'] # Defines a list of strings, where 'Football' appears twice.

word = 'Football' # Defines the specific string we want to count in the list.

res = sports.count(word) # Uses the built-in list method .count() to find the number of times 'word' appears in the 'sports' list and stores the result in the 'res' variable.

print(f'{res} times appear the {word}') # Prints the final count to the console using an f-string for formatted output.
