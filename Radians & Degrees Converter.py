# Made by Sovf!

import math

print("Welcome to Radians & Degrees Converter!\n\nThese are Convertions;\n\n1 - Degrees to Radians\n2 - Radians to Degrees\n")

Tbl = [None, math.radians, math.degrees]

while True:
    Convertion = int(input("Convertion: "))
    Number = float(input("Number: "))

    print("Calculation:", Tbl[Convertion](Number), "\n")
