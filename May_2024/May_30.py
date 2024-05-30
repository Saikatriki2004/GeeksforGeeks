class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        MOD = int(1e9 + 7)
        n = len(s1)
        m = len(s2)
        
        # Initialize the DP table with all 0's
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base cases
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j] % MOD
        
        return dp[n][m]

# Example usage:
solution = Solution()
print(solution.countWays("geeksforgeeks", "gks"))  # Output: 4
print(solution.countWays("problemoftheday", "geek"))  # Output: 0
