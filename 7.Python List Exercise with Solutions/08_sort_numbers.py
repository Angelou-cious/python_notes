numbers = [5, 2, 8, 1, 9] # This line initializes a list of integers. The elements are in an arbitrary order.

print(f'Original List: {numbers}') # This line prints the original, unsorted list to the console. The f-string is used for easy formatting.

sorted_list = sorted(numbers) # This line calls the built-in `sorted()` function, which takes the `numbers` list as an argument and returns a new list with the elements sorted in ascending order. The original `numbers` list remains unchanged.

print(f'Sorted List: {sorted_list}') # This line prints the new `sorted_list` to the console, showing the numbers in their sorted order.
