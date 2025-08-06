word = str(input(f'Enter a word: '))
number = int(input(f'Enter a number: '))


print(f'|{word:10}{number}|') # right aligned (default)
print(f'|{word:>10}{number}|') # left aligned
print(f'|{word:^10}{number}|') # center aligned