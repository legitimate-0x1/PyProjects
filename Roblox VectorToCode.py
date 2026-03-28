# Made by Sovf!

print("Welcome to Vector3 Converter\n")

def IntNumber(Value):
    try:
        IntValue = int(Value)
        
        return IntValue == Value and IntValue or Value
    except:
        return Value

class VectorToCode:
    def Vector2(X, Y):
        X, Y = str(X), str(Y)
        
        return X == Y and (X == "0" and "Vector2.zero" or "Vector2.new("+X+")") or "Vector2.new("+X+", "+Y+")"
        
    def Vector2int16(X, Y):
        X, Y = str(X), str(Y)
        
        return X == Y and "Vector2int16.new("+X+")" or "Vector2int16.new("+X+", "+Y+")"
        
    def Vector3(X, Y, Z):
        X, Y, Z = str(X), str(Y), str(Z)
        
        return X == Y == Z and (X == "0" and "Vector3.zero" or "Vector3.new("+X+")") or "Vector3.new("+X+", "+Y+", "+Z+")"
        
    def Vector3int16(X, Y, Z):
        X, Y, Z = str(X), str(Y), str(Z)
        
        return X == Y == Z and "Vector3int16.new("+X+")" or "Vector3int16.new("+X+", "+Y+", "+Z+")"
        
    def tonumber(Value):
         try:
             Value = float(Value)
             
             return IntNumber(Value)
         except:
             return None
             
