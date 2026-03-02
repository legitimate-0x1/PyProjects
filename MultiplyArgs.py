# Made by Sovf!

def MultiplyArgs(*Args):
    Tbl = []

    for Index in Args:
        Tbl.append(Index * 2)

    return Tbl

print(MultiplyArgs(1, 2, 3)) # --> [2, 4, 6]
