# Import the 'string' module. This module contains a collection of string constants,
# including 'punctuation', which is a string containing all ASCII characters considered punctuation.
import string

# Define a function named 'remove_punctuation' that takes one argument, 'str_input'.
# This function is designed to clean up a string by removing punctuation and replacing '&'.
def remove_punctuation(str_input):

    # The 'split()' method breaks the input string 'str_input' into a list of words.
    # By default, it splits the string at each whitespace character (like spaces or newlines).
    # For example, "Hello world" becomes ['Hello', 'world'].
    old_list = str_input.split()

    # Initialize an empty list called 'new_list'.
    # This list will store the cleaned words.
    new_list = []

    # Start a 'for' loop that iterates over each word ('stri') in the 'old_list'.
    for stri in old_list:
        
        # Check if the current word ('stri') is exactly equal to the ampersand symbol '&'.
        if stri == '&':
            # If the word is '&', append the string 'and' to our 'new_list'.
            new_list.append('and')

            # The 'continue' keyword tells the loop to stop the current iteration
            # and immediately start the next one. This prevents the '&' from being processed further.
            continue
        
        # 'str.maketrans()' is a method used to create a translation table for the 'translate()' method.
        # The three arguments are:
        # 1st: characters to be replaced
        # 2nd: characters to replace with
        # 3rd: characters to be deleted
        # Here, we are creating a table to delete all characters found in 'string.punctuation'.
        translator = str.maketrans('', '', string.punctuation)

        # The 'translate()' method applies the 'translator' table to the current word 'stri'.
        # It removes all punctuation characters from the word.
        # For example, '/*Jon' becomes 'Jon'.
        no_punctuation = stri.translate(translator)

        # Append the cleaned word ('no_punctuation') to our 'new_list'.
        new_list.append(no_punctuation)

    # After the loop finishes, the 'join()' method is used to combine all the words in 'new_list'
    # into a single string. Each word is separated by a space ' '.
    return ' '.join(new_list)

# Define a string variable 'str1' with some text that includes punctuation and an ampersand.
str1 = "/*Jon is @developer & musician"

# Print the original string to the console, using an f-string for easy formatting.
print(f'Original String: {str1}')

# Call the 'remove_punctuation' function with 'str1' as the input.
# The cleaned string returned by the function is then printed to the console.
print(f'Cleaned String: {remove_punctuation(str1)}')
