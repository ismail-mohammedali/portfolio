class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
       
        for i in range(len(nums)):
            
            if len(nums)==1 or len(nums)-1 ==i:
                return False
            
            if nums[i]==nums[min(i+1,len(nums)-1)]:
                return True
            
        return False
        