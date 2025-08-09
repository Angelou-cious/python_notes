# Exercise: Given the nested list below, write the code to swap the
# first and last elements of the second inner list (the one with 44, 55, 66).

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

print(f'Original List: {nested_list}')

# --- Your code here ---
# Write the code to swap the elements.
nested_list[1][0], nested_list[1][2] = nested_list[1][2], nested_list[1][0]

# ----------------------

print(f'Modified List: {nested_list}')

# Expected output:
# Original List: [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
# Modified List: [[10, 20, 30], [66, 55, 44], [77, 87, 99]]