# Made by Sovf!

def DivideArgs(*Args):
    Tbl = []

    for Index in Args:
        Tbl.append(Index / 2)

    return Tbl

print(DivideArgs(6, 4, 2)) # --> [3.0, 2.0, 1.0]
