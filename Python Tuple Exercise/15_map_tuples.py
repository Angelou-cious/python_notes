# Defines a tuple named 't' with four integer elements.
t = (1, 2, 3, 4)

# Creates a list 'new_tuple' where each item from 't' is squared.
new_tuple = [item ** 2 for item in t]
# Converts the list 'new_tuple' into a tuple.
new_tuple = tuple(new_tuple)
# Creates a new tuple 'nnew_tuple' directly by squaring each item in 't'.
nnew_tuple = tuple(item ** 2 for item in t)
# Prints the original tuple 't'.
print(t)
# Prints the tuple 'new_tuple' with squared numbers.
print(new_tuple)
# Prints the tuple 'nnew_tuple' created directly with squared numbers.
print(nnew_tuple)
