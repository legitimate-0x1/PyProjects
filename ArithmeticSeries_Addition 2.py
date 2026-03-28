# Made by Sovf!

def Concat(Tbl):
    Concatted = ""
    TblCount = len(Tbl)
    
    for Index in Tbl:
        Concatted += str(Index)
        
        if Index != TblCount:
            Concatted += " + "
         
    return Concatted
    
while True:
    Input = int(input("Sayı: "))
    InputPlus = Input + 1
    Tbl = []
    
    for Index in range(1, InputPlus):
        Tbl.append(Index)
        
    Concatted = Concat(Tbl)
    
    print(Concatted, "=", str(int(Input*InputPlus/2)), "\n")
