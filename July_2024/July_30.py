class Solution:
    def findPath(self, mat):
        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n and mat[x][y] == 1
        
        def dfs(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            
            # Mark the cell as visited
            mat[x][y] = 0
            
            # Move Down
            if isSafe(x + 1, y):
                dfs(x + 1, y, path + 'D')
            
            # Move Left
            if isSafe(x, y - 1):
                dfs(x, y - 1, path + 'L')
            
            # Move Right
            if isSafe(x, y + 1):
                dfs(x, y + 1, path + 'R')
            
            # Move Up
            if isSafe(x - 1, y):
                dfs(x - 1, y, path + 'U')
            
            # Unmark the cell as visited (backtrack)
            mat[x][y] = 1
        
        n = len(mat)
        paths = []
        
        # If the starting cell is blocked, return empty list
        if mat[0][0] == 0:
            return paths
        
        dfs(0, 0, "")
        return sorted(paths)

# Example usage:
sol = Solution()
matrix = [[1, 0, 0, 0],
          [1, 1, 0, 1],
          [1, 1, 0, 0],
          [0, 1, 1, 1]]
print(sol.findPath(matrix))  # Output: ['DDRDRR', 'DRDDRR']

matrix2 = [[1, 0],
           [1, 0]]
print(sol.findPath(matrix2))  # Output: []
