from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        # Step 1: Create a graph
        graph = defaultdict(set)
        in_degree = {chr(i + ord('a')): 0 for i in range(K)}
        
        # Step 2: Build the graph by comparing adjacent words
        for i in range(N - 1):
            word1, word2 = alien_dict[i], alien_dict[i + 1]
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Step 3: Perform topological sort (Kahn's Algorithm - BFS)
        queue = deque([ch for ch in in_degree if in_degree[ch] == 0])
        order = []
        
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for neighbor in graph[ch]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we used all characters, return the order, otherwise return ""
        if len(order) == K:
            return ''.join(order)
        else:
            return ""

# Example Usage:
alien_dict = ["baa", "abcd", "abca", "cab", "cad"]
N = 5
K = 4
sol = Solution()
print(sol.findOrder(alien_dict, N, K))  # Expected Output: "bdac" or any valid topological order
