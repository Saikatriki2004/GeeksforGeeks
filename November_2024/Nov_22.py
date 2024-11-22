class Solution:
    def maximumProfit(self, prices):
        # Initialize variables
        min_price = float('inf')  # Minimum price seen so far
        max_profit = 0           # Maximum profit possible
        
        # Iterate through prices
        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            
            # Calculate potential profit and update max_profit
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
