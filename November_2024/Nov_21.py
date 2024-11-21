from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        # Initialize variables to track profit
        max_profit = 0
        
        # Traverse through prices and calculate profit when there's an increase
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
