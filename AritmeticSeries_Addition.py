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
    Number = 0
    Input = int(input("Number: "))
    Tbl = []
    
    for Index in range(1, Input + 1):
        Number += Index
        Tbl.append(Index)
        
    Concatted = Concat(Tbl)
    
    print(Concatted, "=", str(Number), "\n")
