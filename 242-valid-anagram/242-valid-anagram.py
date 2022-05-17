class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False
        
        s_ang,t_ang = {},{}
        
        for i in range(len(s)):
            s_ang[s[i]]=1 + s_ang.get(s[i],0)
            t_ang[t[i]]=1 + t_ang.get(t[i],0)
        for car in s_ang: 
            if s_ang[car]!=t_ang.get(car,0):
                return False
        return True
        
        