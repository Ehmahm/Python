
#QN.2
import random

numb_to_guess = random.randint(1, 20)
while True:
    guess = int(input("Guess the number between 1 and 20: "))
    if guess == numb_to_guess:
        print("Well guessed!")
        break



#QN.4
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

#QN.10
m = int(input("Input number of rows: "))
n = int(input("Input number of columns: "))
array = [[i * j for j in range(n)] for i in range(m)]
print(array)


#12
string = input("Enter a string: ")
uppercase_count = sum(1 for c in string if c.isupper())
lowercase_count = sum(1 for c in string if c.islower())
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)

#QN.13
import re

password = input("Enter a password: ")
if (6 <= len(password) <= 16 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$%&]", password)):
    print("Valid password")
else:
    print("Invalid password")

#QN.39
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#QN.50
def nest_num(num):
    for i in range(num):
        for j in range(i, -1, -1):
            print(j, end = "")

nest_num(10)

#QN.1
numbers = [x for x in range(2000, 3201) if x % 8 == 0 and x % 6 == 0]
print(numbers)



#QN.5
numbers = [13, 26, 39, 52, 65, 78, 91]
divisible_by_13 = [x for x in numbers if x % 13 == 0]
print("Number of numbers divisible by 13:", len(divisible_by_13))


#QN.7
for i in range(11):
    if i == 4 or i == 8:
        continue
    print(i, end=" ")
print()

