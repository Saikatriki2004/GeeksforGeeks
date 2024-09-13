# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root: Node) -> None:
        # Base case: if the tree is empty, do nothing
        if root is None:
            return
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively mirror the left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
