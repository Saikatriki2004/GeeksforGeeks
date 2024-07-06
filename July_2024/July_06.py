class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    def __init__(self):
        self.prev = None

    def populateNext(self, root):
        # Function to traverse the tree in in-order and populate the next pointers
        if root:
            # Traverse the left subtree
            self.populateNext(root.left)

            # Set the next of the previous node to the current node
            if self.prev:
                self.prev.next = root

            # Update the previous node to the current node
            self.prev = root

            # Traverse the right subtree
            self.populateNext(root.right)

# Example Usage:
# Creating a binary tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

# Creating a solution object and populating next pointers
solution = Solution()
solution.populateNext(root)

# Testing the result by printing the next of each node
def print_in_order_with_next(node):
    if node:
        print_in_order_with_next(node.left)
        next_val = node.next.data if node.next else None
        print(f"Node {node.data} -> Next {next_val}")
        print_in_order_with_next(node.right)

print_in_order_with_next(root)
