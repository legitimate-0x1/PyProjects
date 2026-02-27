# Made by legitimate0x1!

import time

print("Welcome to Number Countdown!\n")

while True:
    Countdown, Cooldown = int(input("Countdown: ")), float(input("Cooldown: "))

    for Index in range(Countdown, -1, -1):
        print(Index)
        time.sleep(Cooldown)
