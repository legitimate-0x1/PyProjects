# Made by legitimate0x1!

print("Welcome to Math Calculator!\n")

def Add(Number, Number2):
    return Number + Number2

def Subtract(Number, Number2):
    return Number - Number2

def Multiply(Number, Number2):
    return Number * Number2

def Divide(Number, Number2):
    return Number / Number2

MathOperators = [None, Add, Subtract, Multiply, Divide]

print("Welcome to 2 Num Math Calculator!\n\nMath Operators;\n\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n")

while True:
    Input, Input2, MathOperatorIndex = float(input("Number: ")), float(input("Number 2: ")), int(input("Math Operator: "))

    if MathOperatorIndex > 4 or MathOperatorIndex < 1:
        print("Invalid Math Operator selected!")
        continue

    print(MathOperators[MathOperatorIndex](Input, Input2), "\n")
