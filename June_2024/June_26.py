class Solution:
    def sumOfCoverage(self, matrix):
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        coverage_sum = 0

        # Directions: left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                            coverage_sum += 1
        
        return coverage_sum

# Example usage:
sol = Solution()
matrix1 = [[0, 1, 0], [0, 1, 1], [0, 0, 0]]
print(sol.sumOfCoverage(matrix1))  # Output: 6

matrix2 = [[0, 1]]
print(sol.sumOfCoverage(matrix2))  # Output: 1
