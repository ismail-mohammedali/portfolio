class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        lowest = prices[0]
        
        for i in range(len(prices)):
            if lowest>prices[i]:
                lowest = prices[i]
            curent_max = prices[i]-lowest
            max_profit = max(max_profit,curent_max)
        return max_profit
            
        
        