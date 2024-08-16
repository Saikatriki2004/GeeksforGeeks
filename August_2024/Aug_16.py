class Solution:
    
    # Function to find the maximum number of cuts.
    def maximizeTheCuts(self, n, x, y, z):
        # Initialize the dp array with -1
        dp = [-1] * (n + 1)
        
        # Base case: No cuts needed for a segment of length 0
        dp[0] = 0
        
        # Iterate over each length from 1 to n
        for i in range(1, n + 1):
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        
        # If no valid cuts could be made, return 0
        return max(0, dp[n])

# Example usage:
sol = Solution()
print(sol.maximizeTheCuts(4, 2, 1, 1))  # Output: 4
print(sol.maximizeTheCuts(5, 5, 3, 2))  # Output: 2
