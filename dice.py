import random

tries = 0

def roll_dice_until_doubles():
    global tries  # Declare tries as global
    
    doubles = False

    while not doubles:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        print(f'Rolled {roll1} and {roll2}')

        if roll1 == roll2:
            print(f'Doubles! in {tries} tries!')
            doubles = True

        tries += 1

roll_dice_until_doubles()
