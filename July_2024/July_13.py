from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Create an adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Initialize Dijkstra's algorithm
        dist = [float('inf')] * (n + 1)
        dist[1] = 0
        parent = [-1] * (n + 1)
        min_heap = [(0, 1)]  # (distance, node)
        
        while min_heap:
            d, u = heapq.heappop(min_heap)
            
            if d > dist[u]:
                continue
            
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heapq.heappush(min_heap, (dist[v], v))
        
        # Step 3: Check if there's a path to node n
        if dist[n] == float('inf'):
            return [-1]
        
        # Step 4: Reconstruct the path
        path = []
        current = n
        while current != -1:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        
        # Step 5: Return the result
        return [dist[n]] + path

# Example usage:
# sol = Solution()
# print(sol.shortestPath(6, 5, [[2, 5, 6], [1, 4, 4], [3, 6, 1], [4, 5, 5], [1, 2, 2]]))
