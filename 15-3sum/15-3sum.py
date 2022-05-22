class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
       
        result=[]
        for n,a in enumerate(nums):
            if n>0 and a==nums[n-1]:
                continue
            
            left, right= n+1,len(nums)-1
            while left<right:
                cur_sum = a+nums[left]+nums[right]
                if cur_sum == 0: 
                    result.append([a,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif cur_sum >0:
                    right -=1
                elif cur_sum<0:
                    left +=1
        return result
            
            