class Solution:
    def celebrity(self, mat):
        n = len(mat)
        candidate = 0

        # Step 1: Find the candidate
        for i in range(1, n):
            if mat[candidate][i] == 1:  # candidate knows i, so candidate cannot be a celebrity
                candidate = i

        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know i, and i should be known by everyone else
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate

# Example usage:
solution = Solution()
mat1 = [[0, 1, 0], 
        [0, 0, 0], 
        [0, 1, 0]]
print(solution.celebrity(mat1))  # Output: 1

mat2 = [[0, 1], 
        [1, 0]]
print(solution.celebrity(mat2))  # Output: -1
