# Exercise 13: Remove all occurrences of a specific item from a list

# Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]  # This is the original list.
new_list = []  # Create an empty list to store the results.
for number in list1:  # Iterate through each number in the original list.
    if number == 20:  # Check if the current number is 20.
        continue  # If it is, skip to the next iteration.
    else:
        new_list.append(number)  # If it's not 20, add it to the new list.
        
print(f'Original lits {list1}')  # Print the original list.
print(f'list without 20 {new_list}')  # Print the new list without the number 20.
