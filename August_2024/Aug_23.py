from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LeftView(root):
    if not root:
        return []
    
    # Using deque for efficient popping from the front
    queue = deque([root])
    left_view = []
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # Capture the first node at this level
            if i == 0:
                left_view.append(node.data)
            
            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return left_view
# Example Tree:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#          \
#           7

# Constructing the tree:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)

# Running the function
print(LeftView(root))  # Output: [1, 2, 4, 7]
