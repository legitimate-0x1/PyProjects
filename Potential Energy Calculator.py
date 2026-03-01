# Made by Sovf!

print("Welcome to Potentia Energy Calculator!\n")

while True:
    Mass = float(input("Mass: "))
    Acceleration = input("Acceleration: ").replace(" ", "")
    Height = float(input("Height: "))

    if Acceleration == "":
        Acceleration = 9.81

    Acceleration = float(Acceleration)

    print("Potential Energy:", Mass * Acceleration * Height, "\n")
