import time

def countdown_timer(sec):

    while sec > 0:

        print(f'Time remaining: {sec} seconds')
        time.sleep(3)
        sec -= 1

    print(f'Times Up!')

countdown_timer(5)