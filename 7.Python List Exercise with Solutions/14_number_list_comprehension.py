
# Use list comprehension to create a new list containing only the numbers from a given list.

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6] # This is the original list containing numbers and strings.
cleaned_list = [] # This is an empty list that will store the cleaned numbers.

for i in my_list: # This loop iterates through each item in the original list.
    if isinstance(i, str): # This condition checks if the item is a string.
        continue # If the item is a string, the loop skips to the next item.
    else: # If the item is not a string, it must be a number.
        cleaned_list.append(i) # The number is added to the cleaned list.

print(f'Original List: {my_list}') # This line prints the original list.
print(f'Expected List: {cleaned_list}') # This line prints the list with only numbers.
