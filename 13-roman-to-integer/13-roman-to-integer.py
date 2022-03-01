class Solution:
    def romanToInt(self, s: str) -> int:
        def getInt(romanLetter):            
            return{
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
            }[romanLetter] 
        total = 0 
        current = 0
        for char in reversed(s):
            if getInt(char) < current: 
                total-=getInt(char)
                
            else:
                total+=getInt(char)
            current=getInt(char)
            
        return total
            
        
    
        