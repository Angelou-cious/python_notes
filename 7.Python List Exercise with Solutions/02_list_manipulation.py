
my_list = [10, 20, 30, 40, 50] # Create a list named my_list with initial integer values.
print(f'Initial list: {my_list}') # Print the initial list to the console.

my_list[1] = 200 # Access the element at index 1 (the second element) and change its value to 200.
print(f'After changing second element: {my_list}') # Print the list after the modification.

my_list.append(600) # Add the value 600 to the end of the list.
print(f'List after appending 600: {my_list}') # Print the list after appending the new value.

my_list.insert(2, 300) # Insert the value 300 at index 2 of the list.
print(f'List after inserting 300: {my_list}') # Print the list after the insertion.

my_list.remove(600) # Remove the first occurrence of the value 600 from the list.
print(f'List after removing 600 (by value): {my_list}') # Print the list after the removal.

my_list.pop(0) # Remove the element at index 0 from the list.
print(f'List after removing element at index 0: {my_list}') # Print the final list.
