import string # Imports the 'string' library, which contains a collection of common string constants.

def string_cleaner(lists): # Defines a function named 'string_cleaner' that takes a list of sentences.

    cleaned_sentences = [] # Creates an empty list to store the cleaned sentences.

    translator = str.maketrans('', '', string.punctuation) # Creates a translation table to remove all punctuation.

    for sentences in lists: # Loops through each sentence in the input list.

        words = sentences.split() # Splits the sentence into a list of words.

        cleaned_words = [] # Creates an empty list to store the cleaned words of the current sentence.

        for word in words: # Loops through each word in the list of words.

            if word.startswith('#'): # Checks if the word is a hashtag.
                continue # Skips the current word and moves to the next.

            elif word.startswith('@'): # Checks if the word is a mention.
                cleaned_words.append('[user]') # Replaces the mention with '[user]'.
            else: # If the word is not a hashtag or mention.
                new_word = word.translate(translator) # Removes punctuation from the word.
                cleaned_words.append(new_word) # Adds the cleaned word to the list.

        cleaned_sentences.append(' '.join(cleaned_words)) # Joins the cleaned words back into a sentence.
        
    return cleaned_sentences # Returns the list of fully cleaned sentences.


posts = [ # A list of social media posts to be cleaned.
    "Just learned a lot about #Python string methods! Thanks @awesome_tutor.",
    "This is so cool! #coding #100DaysOfCode",
    "Can't wait to apply this to my projects. What do you think @another_dev?"
]


print(f'Original Posts:') # Prints a header for the original posts.
for post in posts: # Loops through and prints each original post.
    print(post)

print(f'Cleaned Posts:') # Prints a header for the cleaned posts.
for i, post in enumerate(string_cleaner(posts)): # Loops through the cleaned posts, with an index.
    print(f'Sentence {i+1}: {post}') # Prints each cleaned sentence with its number.
