class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def RemoveHalfNodes(self, node):
        if node is None:
            return None

        # Recursively remove half nodes from the left and right subtrees
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)

        # If the current node is a half node with only left child, return left child
        if node.left is not None and node.right is None:
            return node.left

        # If the current node is a half node with only right child, return right child
        if node.right is not None and node.left is None:
            return node.right

        # If the current node is a full node or a leaf node, return it as is
        return node

# Helper function to perform inorder traversal
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Example usage:
if __name__ == "__main__":
    # Construct the tree
    root = Node(5)
    root.left = Node(7)
    root.right = Node(8)
    root.left.left = Node(2)

    # Create a Solution object
    solution = Solution()

    # Remove half nodes
    root = solution.RemoveHalfNodes(root)

    # Print inorder traversal of the modified tree
    print("Inorder traversal of the modified tree:")
    print(inorder_traversal(root))  # Output: [2, 5, 8]
