class Solution:
    def reverse(self, x: int) -> int:
        
        neg_num = 1 
        if x < 0:
            x = abs(x)
            print("it is negetive num")
            neg_num = -abs(neg_num)
           
        new_x=int(str(x)[::-1])
        
        
        if new_x<=2**31:
            return new_x*neg_num
        else: 
            return 0
        