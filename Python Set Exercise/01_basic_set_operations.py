"""
    Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.

    Add Element: Add “grape” to the fruits set.
    
    Remove Element: Remove “banana” from the fruits set.

    Discard Element: Try to discard “mango” from the fruits set.

    1. After creating the set: {'apple', 'orange', 'mango', 'banana'}
    2. After adding 'grape': {'orange', 'banana', 'grape', 'apple', 'mango'}
    3. After removing 'banana': {'orange', 'grape', 'apple', 'mango'}
    4. After discarding 'mango': {'orange', 'grape', 'apple'}
"""

# Create a set named s1 with initial string elements.
s1 = {"apple", "banana", "mango", "orange"}

# Print the initial set to the console.
print(f"1. After creating the set: {s1}")
# Add the string "grape" to the set s1.
s1.add("grape")


# Print the set after adding the new element.
print(f"2. After adding 'grape': {s1}")
# Remove the element "banana" from the set. This will raise a KeyError if "banana" is not in the set.
s1.remove("banana")


# Print the set after removing "banana".
print(f"3. After removing 'banana': {s1}")
# Discard the element 'mango' from the set. This will not raise an error if 'mango' is not in the set.
s1.discard('mango')

# Print the final state of the set after discarding 'mango'.
print(f"4. After discarding 'mango': {s1}")
