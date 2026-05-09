# Project 2 — Number Guessing Game
# Author: Davud Azizi

import random

secret = random.randint(1, 10)
guesses = 0

guess = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    guesses += 1

    if guess < secret:
        guess = int(input("Too low! Try again: "))
    else:
        guess = int(input("Too high! Try again: "))

guesses += 1
print(f"Correct! You got it in {guesses} guesses.")
