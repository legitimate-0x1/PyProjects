# Made by Sovf!

import time

print("Welcome to Countdown!\n")

while True:
    Countdown = int(input("Countdown: "))
    Cooldown = float(input("Cooldown: "))

    print("\n")

    for Index in range(Countdown, -1, -1):
        print(Index)
        time.sleep(Cooldown)

    print("\n")
