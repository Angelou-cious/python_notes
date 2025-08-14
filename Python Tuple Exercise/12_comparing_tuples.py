"""
    Exercise 12: Comparing Tuples

    Compare two tuples and find out which one is “greater” and why?
"""

# Define the first tuple, t1.
t1 = (1, 2, 5, 9)
# Define the second tuple, t2.
t2 = (1, 2, 4, 5)

# When comparing tuples, Python performs an element-wise comparison from left to right.
# The comparison stops as soon as it finds two elements that are different.
# In this case, it compares t1[0] with t2[0] (1==1), then t1[1] with t2[1] (2==2).
# Finally, it compares t1[2] with t2[2] (5 > 4), so t1 is considered greater than t2.
# The comparison does not proceed to the last element.
if t1 > t2:
    # This block executes if t1 is greater than t2.
    print(f"{t2} is less than {t1}")
else:
    # This block executes if t1 is not greater than t2.
    print(f"{t1} is less than {t2}")
