# Node class as provided
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):
        # Initialize pointers for head and previous node
        self.prev = None
        self.head = None

    def bToDLL(self, root):
        # Helper function to perform in-order traversal and convert to DLL
        if not root:
            return
        
        # Recursively convert the left subtree
        self.bToDLL(root.left)

        # Process the current node
        if self.prev is None:
            # If this is the first node, it will be the head of the DLL
            self.head = root
        else:
            # Link the previous node with the current node
            root.left = self.prev
            self.prev.right = root
        
        # Update the previous node to the current node
        self.prev = root

        # Recursively convert the right subtree
        self.bToDLL(root.right)

        # Return the head of the DLL (which will be set during the first call)
        return self.head
