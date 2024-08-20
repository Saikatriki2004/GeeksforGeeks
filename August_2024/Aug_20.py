from collections import deque, defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def minTime(self, root, target):
        if not root:
            return 0

        # Step 1: Create a parent map and find the target node.
        parent_map = {}
        target_node = None

        def map_parents(node, parent=None):
            nonlocal target_node
            if node:
                if node.data == target:
                    target_node = node
                parent_map[node] = parent
                map_parents(node.left, node)
                map_parents(node.right, node)

        map_parents(root)

        # Step 2: Perform BFS from the target node.
        visited = set()
        queue = deque([(target_node, 0)])
        max_time = 0

        while queue:
            current_node, time = queue.popleft()
            visited.add(current_node)
            max_time = max(max_time, time)

            # Explore children
            for neighbor in (current_node.left, current_node.right, parent_map[current_node]):
                if neighbor and neighbor not in visited:
                    queue.append((neighbor, time + 1))

        return max_time
