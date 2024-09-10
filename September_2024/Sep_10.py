class Solution:
    def isCircle(self, arr):
        from collections import defaultdict

        # Create adjacency list based on the first and last character of each string
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        graph = defaultdict(list)

        # Build the graph
        for word in arr:
            start, end = word[0], word[-1]
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Check if in-degree and out-degree are balanced for all characters
        for node in set(in_degree) | set(out_degree):
            if in_degree[node] != out_degree[node]:
                return 0  # If they are not equal, circle is not possible
        
        # Function to perform DFS
        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        # Start DFS from the first character of the first word
        visited = set()
        start_char = arr[0][0]
        dfs(start_char, visited)
        
        # Check if all unique characters were visited (graph is connected)
        unique_chars = set(in_degree.keys()) | set(out_degree.keys())
        if len(visited) == len(unique_chars):
            return 1
        else:
            return 0

# Example usage
solution = Solution()
arr = ["abc", "cde", "efg", "gha"]
print(solution.isCircle(arr))  # Output will depend on whether the words form a circle
