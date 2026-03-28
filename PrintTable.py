# Made by Sovf!

def PrintTable(Table):
    if isinstance(Table, (dict, list)):
        for Index in Table:
            print(Index)
            PrintTable(Index)
            
PrintTable([1, 2, [3]])
