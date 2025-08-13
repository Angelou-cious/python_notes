"""
    Exercise 16: Count Unique Words

    Write a code to count the number of unique words in the given a sentence.
"""

sentence = "Dog is a simple animal dogs is selfless Animal"  # This line initializes a string variable named 'sentence' with a sample text.

sentence = sentence.lower().split()  # This line converts all characters in the sentence to lowercase to ensure case-insensitive matching, and then splits the sentence into a list of words.

unique_word = set(sentence)  # This line converts the list of words into a set. Sets in Python automatically store only unique elements, effectively removing any duplicate words.

print(f"Number of unique words: {len(unique_word)}")  # This line prints the number of unique words by calculating the length of the set.
