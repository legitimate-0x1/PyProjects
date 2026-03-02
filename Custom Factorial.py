# Made by Sovf!

def Factorial(Number):
    Calculated = 1

    for Index in range(1, Number + 1):
        Calculated *= Index

    return Calculated

print(Factorial(3)) # --> 6
