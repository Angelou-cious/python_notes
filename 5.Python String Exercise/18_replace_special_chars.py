# Exercise 18: Replace each special symbol with # in the following string
import string  # Import the string module to access punctuation characters.

input_string = '/*Jon is @developer & musician!!'  # Define the input string with special characters.

print(f'Original input: {input_string}')  # Print the original string.

print(f'Expected output: ##Jon is #developer # musician##')  # Print the expected output for reference.

def replace_special_symbols(text):  # Define a function to replace special symbols.

    word_list = text.split()  # Split the input text into a list of words.

    cleaned_words = []  # Initialize an empty list to store words with replaced symbols.

    # Create a translation table to map each punctuation character to a '#'.
    translator = str.maketrans(string.punctuation, '#' * len(string.punctuation))

    for word in word_list:  # Iterate through each word in the list.
        
        cleaned_word = word.translate(translator)  # Replace punctuation in the word using the translator.

        cleaned_words.append(cleaned_word)  # Add the cleaned word to the list.

    return ' '.join(cleaned_words)  # Join the cleaned words back into a single string.

# Call the function and print the result.
print(f'New output with replacements: {replace_special_symbols(input_string)}')
