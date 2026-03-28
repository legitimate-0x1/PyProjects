# Made by Sovf!

class GenerateSEnv:
    def __init__(self):
        object.__setattr__(self, 'SEnv', {})
    
    def __getattr__(self, Key):
        return self.SEnv.get(Key)
        
    def __setattr__(self, Key, Value):
        self.SEnv[Key] = Value
    
SEnv = GenerateSEnv()

def GetSEnv():
    return SEnv
    
getsenv = GetSEnv

GetSEnv().Number = 5
GetSEnv().Number2 = 5

print(GetSEnv().Number + GetSEnv().Number2) # 10
