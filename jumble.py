# Word Jumble
import random

words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]	

word = random.choice(words)

print(word)

jumbled = list(word)

print(jumbled)

random.shuffle(jumbled)

print("Unscramble:", ''.join(jumbled))

# Let someone guess the word and we confirm if it is correct. Give them a shout if its correct
guess = input("Your guess: ")

if guess == word:
    print("Correct!")
else:
    print("Incorrect!")