import heapq

class Solution:
    """
    This class provides a solution to the minimum cost path problem.
    """
    
    def minimumCostPath(self, grid):
        """
        This method calculates the minimum cost to reach the bottom-right cell in the grid.
        
        Args:
        grid (list of lists): A 2D grid of integers representing the cost to reach each cell.
        
        Returns:
        int: The minimum cost to reach the bottom-right cell.
        """
        
        # Get the number of rows and columns
        n = len(grid)
        
        # Directions for moving in the grid (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Priority queue to store (cost, x, y)
        pq = [(grid[0][0], 0, 0)]
        
        # Initialize distance array with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        
        while pq:
            current_cost, x, y = heapq.heappop(pq)
            
            # If we reached the bottom-right cell, return the cost
            if x == n-1 and y == n-1:
                return current_cost
            
            # Explore all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = current_cost + grid[nx][ny]
                    
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
        
        return dist[n-1][n-1]
