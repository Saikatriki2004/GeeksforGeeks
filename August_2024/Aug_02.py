class Solution:
    def editDistance(self, str1, str2):
        m = len(str1)
        n = len(str2)
        
        # Create a DP array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the base cases
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from str1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters to str1
        
        # Fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],    # Remove
                                   dp[i][j-1],    # Insert
                                   dp[i-1][j-1])  # Replace
                    dp[i][j] += 1
        
        return dp[m][n]

# Example usage:
solution = Solution()
str1 = "geek"
str2 = "gesek"
print(solution.editDistance(str1, str2))  # Output: 1

str1 = "gfg"
str2 = "gfg"
print(solution.editDistance(str1, str2))  # Output: 0
