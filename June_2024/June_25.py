class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0
        k = k % m  # Reduce the number of rotations

        if k == 0:
            return mat

        # Rotating the matrix using list comprehension
        rotated_mat = [row[k:] + row[:k] for row in mat]
        
        return rotated_mat

# Example usage:
sol = Solution()
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k1 = 1
result1 = sol.rotateMatrix(k1, mat1)
for row in result1:
    print(" ".join(map(str, row)))
# Output: 
# 2 3 1
# 5 6 4
# 8 9 7

mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k2 = 2
result2 = sol.rotateMatrix(k2, mat2)
for row in result2:
    print(" ".join(map(str, row)))
# Output: 
# 3 1 2
# 6 4 5
# 9 7 8
