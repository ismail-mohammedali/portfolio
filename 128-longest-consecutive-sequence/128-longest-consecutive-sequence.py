class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0 
        for n in nums: 
            if (n-1) not in set_nums: 
                sequance_count = 0 
                while (n + sequance_count) in set_nums: 
                    sequance_count +=1
                    longest = max(longest,sequance_count)
                    
        return longest
        
        