class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findAncestors(self, root, target):
        # Helper function to perform DFS
        def dfs(node, target):
            if not node:
                return False
            # If the current node is the target, return True
            if node.data == target:
                return True
            # Recur for left and right subtrees
            if dfs(node.left, target) or dfs(node.right, target):
                # If the target is found in either subtree, add current node to ancestors
                ancestors.append(node.data)
                return True
            return False

        # List to store ancestors
        ancestors = []
        # Initialize the DFS traversal
        dfs(root, target)
        return ancestors

# Example usage:
# Constructing the binary tree:
#          78
#        /    \
#       4      81
#      / \       \
#    21   52     77
#   / \   / \      \
#  50 15 82 70    56
# /  \         \
#11   99       38
#   /
#  29

root = Node(78)
root.left = Node(4)
root.right = Node(81)
root.left.left = Node(21)
root.left.right = Node(52)
root.right.right = Node(77)
root.left.left.left = Node(50)
root.left.left.right = Node(15)
root.left.right.left = Node(82)
root.left.right.right = Node(70)
root.right.right.right = Node(56)
root.left.left.left.left = Node(11)
root.left.left.left.right = Node(99)
root.right.right.right.right = Node(38)
root.left.left.left.right.left = Node(29)

sol = Solution()
target = 56
print(sol.findAncestors(root, target))  # Output: [77, 81, 78]

target = 78
print(sol.findAncestors(root, target))  # Output: []

target = 21
print(sol.findAncestors(root, target))  # Output: [4, 78]
