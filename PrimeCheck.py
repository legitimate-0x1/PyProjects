# Made by Sovf!

print("Welcome to Number Primality Checker!\n")

def PrimeCheck(Number):
    IsPrime = True

    for Index in range(2, 10):
        if Number % Index == 0 and Number != Index:
            IsPrime = False

    return IsPrime

while True:
    Number = int(input("Number: "))
    print(Number, "Primality:", (PrimeCheck(Number) and "Prime" or "Nonprime"), "\n")
