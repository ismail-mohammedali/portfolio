class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0 
        l,r = 0,1 
        while r < len(prices):
            if prices[l]< prices [r]:
                profit = prices[r] - prices[l]
                current_max = max(current_max,profit)
            else: 
                l=r
            r+=1
        return current_max
                
                
        