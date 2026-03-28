# Made by Sovf!

def PrintTableElements(Val):
    if isinstance(Val, (dict, list)):
        for Index in Val:
            PrintTableElements(Index)
    else:
         print(Val)
            
PrintTableElements([1, 2, [3]])
