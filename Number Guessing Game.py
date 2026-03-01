# Made by Sovf!

import random

print("Welcome to Number Guessing Game!\n")

while True:
    Number = random.randint(1, 10)

    print("Guess the number between 1 and 10!")
    print((int(input("Pick a Number: ")) == Number and "You guessed It correct" or ("You failed! It was " + str(Number))) + "!\n")
