def has_int(str):

    for i in str:
        if '0' <= i <= '9': # checks if the i is a digit between 0 and 9 — but as a character, not a number.
            return True
    return False

while True:

    user = str(input(f'Enter a string: '))

    if has_int(user):
        print(f'The string contains at least one digit.')
    else:
        print(f'The string does not contain any digits.')
          
    exit = input(f'exit? (Y) if yes (N) if no')

    if exit == 'Y':
        break # close the loop
    else:
        continue
