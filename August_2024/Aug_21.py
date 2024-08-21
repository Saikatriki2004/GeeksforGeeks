#Shortest path in Undirected Graph:
from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Create an adjacency list for the graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Initialize distance array
        dist = [float('inf')] * n
        dist[src] = 0
        
        # BFS initialization
        q = deque([src])
        
        while q:
            node = q.popleft()
            
            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
        
        # Replace infinity with -1 for unreachable nodes
        dist = [-1 if d == float('inf') else d for d in dist]
        
        return dist

# Example usage:
edges = [
    [0, 1], [0, 3], [3, 4], [4, 5], [5, 6],
    [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]
]
n = 9  # Number of nodes
m = 10 # Number of edges
src = 0 # Source node
ob = Solution()
ans = ob.shortestPath(edges, n, m, src)
print(" ".join(map(str, ans)))
