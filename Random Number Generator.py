# Made by Sovf!

import random

print("Welcome to Random Number Generator!\n")

while True:
    NumberA = int(input("Number A: ")) + 1
    NumberB = int(input("Number B: ")) - 1

    if NumberA > NumberB or NumberA == NumberB:
        print("Number A is greater than Number B or equal to It!\n")
        continue

    print("Number A - Number B (Between):", random.randint(NumberA, NumberB - 1), "\n")
