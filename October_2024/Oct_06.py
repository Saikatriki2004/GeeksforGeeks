class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])

        # Directions for 8 possible moves (including diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def iterative_dfs(r, c):
            # Use a stack instead of recursion to avoid stack overflow
            stack = [(r, c)]
            grid[r][c] = 0  # Mark the starting land as visited (set to 0)
            
            while stack:
                cr, cc = stack.pop()
                
                # Explore all 8 directions
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0  # Mark as visited
                        stack.append((nr, nc))

        num_islands = 0
        
        # Iterate over all the cells in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_islands += 1
                    iterative_dfs(r, c)
        
        return num_islands
