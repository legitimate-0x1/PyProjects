# Made by Sovf!

import base64

print("Welcome to Base64 Converter!\n\nThese are Convertions;\n\n 1 - String to Base64\n 2 - Base64 to String\n\n")

Tbl = [None, base64.b64encode, base64.b64decode]

while True:
    Convertion = int(input("Convertion: "))

    if Convertion not in Tbl:
        print("Convertion is not found!\n")
        continue
    
    Input = input("Dat: ")
    Converted = Tbl[Convertion](Input.encode()).decode()

    print("Output:", Converted, "\n")
