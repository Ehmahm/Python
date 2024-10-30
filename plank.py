import time

def countdown(seconds):
    while seconds > 0:
        print('Second', seconds)
        seconds -= 1
        time.sleep(1)

    print('Blastoff!')

print('Enter Duration of your plank in Seconds')
seconds = int(input())

countdown(seconds)