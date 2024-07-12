class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: Node, target: int) -> bool:
        if not root:
            return False
        
        # If it's a leaf node
        if not root.left and not root.right:
            return root.data == target
        
        # Subtract the current node's value from the target sum
        target -= root.data
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)

# Example usage:
# Constructing the binary tree:
#         1
#       /   \
#      2     3

root = Node(1)
root.left = Node(2)
root.right = Node(3)

sol = Solution()
target1 = 2
print(sol.hasPathSum(root, target1))  # Output: False

target2 = 4
print(sol.hasPathSum(root, target2))  # Output: True
