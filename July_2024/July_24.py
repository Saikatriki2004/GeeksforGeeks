class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    """
    This class defines a method to check if a binary tree is a Binary Search Tree (BST).
    """

    def isBST(self, root):
        """
        Checks if a given binary tree is a Binary Search Tree (BST).

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is a BST, False otherwise.
        """
        def isBSTUtil(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True  # Empty subtree is considered valid

            if node.data <= min_val or node.data >= max_val:
                return False  # Node value violates BST property

            return isBSTUtil(node.left, min_val, node.data) and isBSTUtil(node.right, node.data, max_val)

        # Start the check from the root node with minimum allowed value as negative infinity
        # and maximum allowed value as positive infinity
        return isBSTUtil(root)

# Helper function to build the tree from input list
def buildTree(values):
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if index < len(values) and values[index] is not None:
            node.left = Node(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = Node(values[index])
            queue.append(node.right)
        index += 1
    return root

# Example input: 2 1 3 N N N 7 6
input_values = [2, 1, 3, None, None, None, 7, 6]
root = buildTree(input_values)

if Solution().isBST(root):
    print("true")
else:
    print("false")
