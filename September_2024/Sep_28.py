class Solution:
    def minimizeCost(self, k, arr):
        # Get the number of stones
        n = len(arr)
        
        # Initialize dp array where dp[i] represents the minimum cost to reach stone i
        dp = [float('inf')] * n
        
        # Starting point, no cost to stand on the first stone
        dp[0] = 0
        
        # Loop through each stone and calculate the minimum cost to reach that stone
        for i in range(1, n):
            # For each stone i, check all possible jumps from stone i-k to i-1
            for j in range(1, min(k, i) + 1):
                dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))
        
        # The minimum cost to reach the last stone is stored in dp[n-1]
        return dp[n - 1]
