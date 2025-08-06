def myfunc(text):

    count = 0
    for i in range(len(text) - len('Emma')):
        if text[i:i+4] == 'Emma':
            count += 1
    print(f'Emma appeared {count} times')


myfunc('Emma is good developer. Emma is a writer')