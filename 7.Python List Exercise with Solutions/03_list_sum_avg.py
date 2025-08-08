# Exercise: Calculate the sum and average of a list of numbers.
my_list = [10, 20, 30, 40, 50] # This line initializes a list of integers.

sum = 0 # This line initializes a variable to store the sum of the list elements, starting from 0.
count = 0 # This line initializes a variable to count the number of elements in the list, starting from 0.

for item in my_list: # This loop iterates through each element in the list.
    sum += item # In each iteration, the current element is added to the `sum` variable.
    count  += 1 # In each iteration, the `count` is incremented by 1.

average = sum / count # This line calculates the average by dividing the sum of the elements by the total count of elements.

print(f'Sum: {sum}') # This line prints the calculated sum of the list.
print(f'Average: {average}') # This line prints the calculated average of the list.


# Exercise: Reverse a list.
list1 = [100, 200, 300, 400, 500] # This line initializes a list of integers.

rev_list = list1[::-1] # This line uses slicing to reverse the list. The `[::-1]` slice creates a reversed copy of the list.

print(rev_list) # This line prints the reversed list.



# Exercise: Square each element of a list.
numbers = [1, 2, 3, 4, 5, 6, 7] # This line initializes a list of integers.

res = [] # This line initializes an empty list that will store the squared numbers.

for number in numbers: # This loop iterates through each number in the `numbers` list.
    number = number ** 2 # This line calculates the square of the current number.

    res.append(number) # This line appends the squared number to the `res` list.

print(res) # This line prints the list of squared numbers.


# Exercise: Find the largest and smallest numbers in a list.
data = [8, 2, 15, 1, 9] # This line initializes a list of integers.

largest = data[0] # This line initializes the `largest` variable with the first element of the list.
smallest = data[0] # This line initializes the `smallest` variable with the first element of the list.
for number in data: # This loop iterates through each number in the `data` list.
    if number > largest: # This condition checks if the current number is greater than the current `largest` number.
        largest = number # If the condition is true, the `largest` variable is updated with the current number.
    if number < smallest: # This condition checks if the current number is smaller than the current `smallest` number.
        smallest = number # If the condition is true, the `smallest` variable is updated with the current number.

print(f'Largest number: {largest}') # This line prints the largest number found in the list.
print(f'Smallest number: {smallest}') # This line prints the smallest number found in the list.
