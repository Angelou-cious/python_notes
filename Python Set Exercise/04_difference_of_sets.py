"""
    Exercise 4: Difference of Sets

    Find the difference (set1 - set2). Write a code to returns a new set containing elements that are present in set1 but not in set2.
"""

set1 = {10, 20, 30, 40, 50} # This line initializes a set named set1 with integer values.
set2 = {30, 40, 50, 60, 70} # This line initializes another set named set2 with different integer values.

set3 = set1 - set2 # This line calculates the difference between set1 and set2. 
                   # The resulting set, set3, will contain elements that are in set1 but not in set2.

print(set3) # This line prints the elements of set3, which is the result of the set difference.
