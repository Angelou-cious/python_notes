
# Write a function that takes a list with duplicate elements and returns a new list with only unique elements.

# Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]  # This is the original list with duplicate values.

list_without_duplicates = set(list_with_duplicates)  # Convert the list to a set to automatically remove duplicates.

cleaned_list = list(list_without_duplicates)  # Convert the set back to a list.

print(f'{cleaned_list}')  # Print the cleaned list without duplicates.