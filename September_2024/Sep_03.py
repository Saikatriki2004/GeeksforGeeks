class Solution:
    def minOperations(self, str1: str, str2: str) -> int:
        m, n = len(str1), len(str2)
        
        # Create a DP table for LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Calculate the minimum operations
        lcs_length = dp[m][n]
        min_operations = (m - lcs_length) + (n - lcs_length)
        
        return min_operations
