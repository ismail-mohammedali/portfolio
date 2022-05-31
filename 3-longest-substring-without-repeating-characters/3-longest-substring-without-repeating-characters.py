class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_substring = 0
        unq_ltr = set()
        left = 0 
        for right in range(len(s)):
            while s[right] in unq_ltr:
                unq_ltr.remove(s[left])
                left+=1
            unq_ltr.add(s[right])
            max_substring = max(max_substring,right-left+1)
                
        
        
        
        
        return max_substring 
        