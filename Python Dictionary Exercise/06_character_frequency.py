"""
    Count Character Frequencies

    Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
"""



# string1 = 'Jessa'

# frequency_dict = {}


# for char in string1:

#     frequency_dict[char] = frequency_dict.get(char, 0) + 1

# print(frequency_dict)


# import string
# def word_frequency(sentence):

#     words = sentence.split()

#     translator = str.maketrans('','', string.punctuation)

#     new_dict = {}

#     for word in words:

#         word = word.lower()

#         word = word.translate(translator)

#         new_dict[word] = new_dict.get(word, 0) + 1

#     return new_dict


# sentence = "The quick brown fox jumps over the lazy dog. The dog barks!"
# print(word_frequency(sentence))

def analyze_groceries(lists1):
    # Initialize an empty dictionary to store item counts
    res = {}
    
    # Loop through each item in the input list
    for item in lists1:
        # Update item count using get():
        # - If item exists in dictionary, get its current count
        # - If not, default to 0
        # Then increment count by 1
        res[item] = res.get(item, 0) + 1

    # Find the most frequent item:
    # - max() finds key with highest value
    # - key=res.get specifies to compare dictionary values
    most_frequent = max(res, key=res.get)
    
    # Count unique items by getting dictionary length
    unique_items = len(res)

    # Return results as a dictionary with:
    # - 'counts': all item frequencies
    # - 'most frequent': highest frequency item
    # - 'unique items': count of distinct items
    return {
        "counts": res,
        "most frequent": most_frequent,
        "unique items": unique_items
    }

# Test grocery list
grocery_list = ["apple", "banana", "apple", "orange", "banana", "apple", "milk"]

# Call function and print results
print(analyze_groceries(grocery_list))