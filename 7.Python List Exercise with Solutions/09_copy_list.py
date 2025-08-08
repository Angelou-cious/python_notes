old_list = [10, 20, 30] # This is the original list.

new_list = old_list.copy() # This creates a shallow copy of the original list.

rev_sort_list = sorted(new_list, reverse=True) # This sorts the copied list in descending order.

print(f'Old List: {old_list}') # This prints the original list.
print(f'New List: {rev_sort_list}') # This prints the sorted list.
