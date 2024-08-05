#Bottom View of Binary Tree:
from collections import deque, defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        # Dictionary to store the bottom view of the tree
        hd_node_map = {}

        # Queue to perform level order traversal
        # It stores pairs of node and its horizontal distance
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # Update the dictionary with the node's value at the current horizontal distance
            hd_node_map[hd] = node.data

            # If the node has a left child, add it to the queue with hd - 1
            if node.left:
                queue.append((node.left, hd - 1))

            # If the node has a right child, add it to the queue with hd + 1
            if node.right:
                queue.append((node.right, hd + 1))

        # Extracting the values in increasing order of horizontal distances
        bottom_view = [hd_node_map[hd] for hd in sorted(hd_node_map.keys())]

        return bottom_view

# Example usage:
# Constructing the tree from the example
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Creating an instance of Solution and finding the bottom view
solution = Solution()
print(solution.bottomView(root))  # Output: [5, 10, 4, 14, 25]
