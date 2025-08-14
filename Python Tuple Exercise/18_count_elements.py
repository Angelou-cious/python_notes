"""
    Exercise 18: Count Elements

    Write a code to counts the number of occurrences of item 50 from a tuple.
"""

# Define a tuple named tuple1 with integer elements.
tuple1 = (50, 10, 60, 70, 50)

# Initialize a counter variable to store the count of 50.
counter = 0
# Iterate through each item in the tuple.
for item in tuple1:
    # Check if the current item is equal to 50.
    if item == 50:
        # If it is, increment the counter.
        counter+=1

# Use the built-in count() method to count occurrences of 50.
counter1 = tuple1.count(50)

# Print the result from the manual count.
print(counter)
# Print the result from the count() method.
print(counter1)
