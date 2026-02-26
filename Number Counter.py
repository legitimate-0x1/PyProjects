# Made by legitimate0x1!

import time

while True:
    Number = int(input("Number to count: "))
    Cooldown = float(input("Cooldown: "))

    print("\n")

    for Index in range(1, Number + 1):
        print(Index)
        time.sleep(Cooldown)

    print("\n")
