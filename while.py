import random

# Generate a random number between 1 and 20
secretNumber = random.randint(1, 20)

print('Welcome to Data-frame Class Game!')
print('I am thinking of a number between 1 and 20.')

# Declare integer variable to store the number of guesses
guesses = 0
guess = 0

# Give the player chances using a while loop, while the guess is not true
while guess != secretNumber:
    print('Take a guess.')
    guess = int(input())

    guesses += 1

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

# Check if the guess is correct
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))