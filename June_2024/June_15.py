class Solution:
    def __init__(self):
        self.a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        self.dp = [[[0 for _ in range(26)] for _ in range(3)] for _ in range(4)]
    
    def getCount(self, n):
        # Initialize the dp array for sequences of length 1
        for i in range(4):
            for j in range(3):
                if self.a[i][j] != -1:
                    self.dp[i][j][1] = 1
        
        # Fill the dp array for lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(4):
                for j in range(3):
                    if self.a[i][j] != -1:
                        self.dp[i][j][length] = self.dp[i][j][length - 1]
                        if j + 1 < 3 and self.a[i][j + 1] != -1:
                            self.dp[i][j][length] += self.dp[i][j + 1][length - 1]
                        if j - 1 >= 0 and self.a[i][j - 1] != -1:
                            self.dp[i][j][length] += self.dp[i][j - 1][length - 1]
                        if i + 1 < 4 and self.a[i + 1][j] != -1:
                            self.dp[i][j][length] += self.dp[i + 1][j][length - 1]
                        if i - 1 >= 0 and self.a[i - 1][j] != -1:
                            self.dp[i][j][length] += self.dp[i - 1][j][length - 1]
        
        # Sum up all possible sequences of length n
        ans = 0
        for i in range(4):
            for j in range(3):
                if self.a[i][j] != -1:
                    ans += self.dp[i][j][n]
        
        return ans

# Example usage:
solution = Solution()
print(solution.getCount(1))  # Output: 10
print(solution.getCount(2))  # Output: 36
print(solution.getCount(3))  # Output: <some large number based on the problem statement>
