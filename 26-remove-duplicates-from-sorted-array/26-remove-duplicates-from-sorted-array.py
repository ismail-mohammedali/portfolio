class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
                
        nonDubArrey= list(set(nums))
        nonDubArrey.sort()
        print(nums, nonDubArrey)
        for x in range(len(nonDubArrey)):
            
            nums[x]= nonDubArrey[x]
        print(nums, nonDubArrey)
        for y in range(x+1,len(nums)):
            nums[y]='_'
            
            
        
        return x+1 
        