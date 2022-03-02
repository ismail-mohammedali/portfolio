class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        nums_list=[]
        for x in nums: 
            sum+=x
            nums_list.append ( sum)
            
        return nums_list