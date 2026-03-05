# Made by Sovf!

print("Welcome to Number Primality Checker!\n")

def PrimeCheck(Number):
    IsPrime = True

    if Number == 1:
        return False

    for Index in range(2, 10):
        if Number % Index == 0 and Number != Index:
            IsPrime = False

    return IsPrime

for Index in range(1, 1001):
    if PrimeCheck(Index):
        print(Index)
