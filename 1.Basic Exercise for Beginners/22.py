
def caps_letter(str):

    lst = str.split() # Split into words
    new_words = [] # New list to store capitalized words


    for i in lst:
        capitalized_word = i.capitalize() # Capitalize the word / upper() means to caps all letters
        new_words.append(capitalized_word) # Store to new_word list

    return ' '.join(new_words) # Join all capitalized words



str1 = "pynative.com is for python lovers"

caps_string = caps_letter(str1)

print(f'Capitalized string: {caps_string}')
