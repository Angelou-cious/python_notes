"""
    Exercise 19: Check if all items in the tuple are the same
"""


tuple1 = (45, 45, 45, 45) # Define a tuple named tuple1 with four identical integer elements.
tuple2 = (40, 45, 45, 45) # Define a tuple named tuple2 with four integer elements, where the first element is different from the rest.
res1 = any(item == tuple2[0] for item in tuple2) # Check if any item in tuple2 is equal to its first element (40). This will be True if at least one item is 40.
res2 = all(item == tuple1[0] for item in tuple1) # Check if all items in tuple1 are equal to its first element (45). This will be True since all elements are 45.
res3 = all(item == tuple2[0] for item in tuple2) # Check if all items in tuple2 are equal to its first element (40). This will be False because not all elements are 40.
print(res1) # Print the result of res1, which checks if any item in tuple2 is 40.
print(res2) # Print the result of res2, which checks if all items in tuple1 are the same.
print(res3) # Print the result of res3, which checks if all items in tuple2 are the same as the first element.
