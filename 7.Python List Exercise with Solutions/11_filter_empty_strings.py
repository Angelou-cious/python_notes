# Exercise 11: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"] # This is the original list containing strings, including some empty ones.
filtered_list = [word for word in list1 if word != ''] # This line uses a list comprehension to create a new list called 'filtered_list'. It iterates through each 'word' in 'list1' and includes it in the new list only if the word is not an empty string.

# for word in list1: # This is a traditional for loop that iterates through each 'word' in 'list1'.
#     if word == '': # This condition checks if the current 'word' is an empty string.
#         continue # If the word is empty, the 'continue' statement skips the rest of the loop and moves to the next iteration.
#     else: # If the word is not empty, this block is executed.
#         filtered_list.append(word) # This line adds the non-empty 'word' to the 'filtered_list'.

print(f'Expected output: {filtered_list}') # This line prints the 'filtered_list' to the console, showing the list after the empty strings have been removed.
