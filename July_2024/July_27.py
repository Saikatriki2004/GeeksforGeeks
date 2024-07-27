class Solution:
    def countMin(self, str):
        n = len(str)
        # Create a table to store results of subproblems
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # Build the table. The gap represents the length of the substring
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        
        # The result is the minimum number of insertions for str[0..n-1]
        return dp[0][n - 1]

# Example usage
solution = Solution()
print(solution.countMin("abcd"))  # Output: 3
print(solution.countMin("aa"))    # Output: 0
