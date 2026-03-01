# Made by Sovf!

import math

print("Welcome to Radians & Degrees Converter!\n\nThese are Convertions;\n\n 1 - Degrees to Radians\n 2 - Radians to Degrees\n\nRounding Enabled: Y/N\n")

Tbl = [None, math.radians, math.degrees]

while True:
    Convertion = int(input("Convertion: "))
    RoundEnabled = input("Rounding Enabled: ").upper() == "Y"
    Number = float(input("Number: "))
    Calculation = Tbl[Convertion](Number)

    print("Calculation:", (RoundEnabled and round(Calculation) or Calculation), "\n")
