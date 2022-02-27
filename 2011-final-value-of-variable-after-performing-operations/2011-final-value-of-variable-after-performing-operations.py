class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        finalValue = 0
        for i in operations: 
            if '+' in i:
                finalValue+=1
            else: 
                finalValue-=1
        return finalValue 
        