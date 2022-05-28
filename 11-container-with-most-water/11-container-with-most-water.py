class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0 
        while left < right:
            water_hight = min(height[left],height[right])*(right-left)
            max_water = max(water_hight,max_water) 
            if height[left]>=height[right]:
                right-=1
            else: 
                left+=1
        return max_water
            
        