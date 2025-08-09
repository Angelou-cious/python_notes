# Write a program to add item 7000 after 6000 in the following Python List



def insert_after_item(lst):

    lst[2][2].append(7000) # Add single item to the end
    lst[2][2].insert(3, 8000) # Add single item to the end

    lst[2][2].extend([500, 600, 700, 800, 900]) # Merge multiple items from another list

    lst[2][2].remove(5000) # Delete by value

    lst[2][2].pop(0) # Remove by index (and get the value)

    lst[2][2].sort() # Order the list ascending/descending


    print(lst)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
insert_after_item(list1)