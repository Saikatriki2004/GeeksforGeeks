from typing import List

class Solution:
    def maxSquare(self, n: int, m: int, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        # Initialize the DP table
        dp = [[0] * m for _ in range(n)]
        max_side = 0

        # Fill the dp table
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side

# Example usage:
sol = Solution()

mat1 = [[0, 1, 1, 0, 1], 
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]
print(sol.maxSquare(6, 5, mat1))  # Output: 3

mat2 = [[1, 1], 
        [1, 1]]
print(sol.maxSquare(2, 2, mat2))  # Output: 2

mat3 = [[0, 0], 
        [0, 0]]
print(sol.maxSquare(2, 2, mat3))  # Output: 0
