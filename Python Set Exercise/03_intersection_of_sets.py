"""
    Exercise 3: Intersection of Sets

    Find the intersection of set1 and set2. Write a code to return a new set containing only the elements that are common to both set1 and set2
"""

set1 = {10, 20, 30, 40, 50} # This line initializes a set named set1 with integer values.
set2 = {30, 40, 50, 60, 70} # This line initializes another set named set2 with different integer values.

set3 = set1 & set2 # This line finds the intersection of set1 and set2 using the '&' operator and stores it in set3.

print(set3) # This line prints the resulting set, which contains elements common to both set1 and set2.
