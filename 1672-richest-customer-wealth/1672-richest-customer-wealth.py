class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich_cus = 0 
        for i in accounts: 
            total_bal = sum(i)
            if total_bal> rich_cus:
                rich_cus = total_bal
        return rich_cus
        