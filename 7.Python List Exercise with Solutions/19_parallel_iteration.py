
"""
    Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
"""

def parallel_iteration(a,b):

    reverse_b = b[::-1]

    for x, y in zip(a, reverse_b):
        
        print(f'{x} {y}')

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

parallel_iteration(list1, list2)