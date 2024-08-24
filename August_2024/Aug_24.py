class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val):
        n = len(wt)
        
        # Create a 2D DP table with dimensions (n+1) x (W+1)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
        # Build the DP table in bottom-up manner
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i-1] <= w:
                    # Include the current item and see if it's better than excluding it
                    dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])
                else:
                    # If the current item can't be included, carry forward the previous value
                    dp[i][w] = dp[i-1][w]
        
        # The maximum value is found at dp[n][W]
        return dp[n][W]
solution = Solution()
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
print(solution.knapSack(W, wt, val))  # Output: 220
