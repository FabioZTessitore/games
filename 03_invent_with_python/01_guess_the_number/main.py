# main.py

# Guess The Number

# Guess a number between 1 and 20. Only six guesses!

# Hello! What is your name?
# Albert
# Well Albert, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too high.
# Take a guess.
# 2
# Your guess is too low.
# Take a guess.
# 4
# Good job, Albert! You guessed my number in 3 guesses!

import random

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well ' + name + ', I am thinking of a number between 1 and 20.')

for counter in range(6):
    print('Take a guess.')
    guess = int(input())
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print('Good job, ' + name + '! You guessed my number in ' + str(counter+1) + ' guesses!')
else:
    print('The number was ' + str(number))