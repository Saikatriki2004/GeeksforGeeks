from collections import deque

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert(head):
    if not head:
        return None
    
    # Initialize the root of the binary tree
    root = TreeNode(head.data)
    
    # Create a queue to hold tree nodes
    queue = deque([root])
    
    # Pointer to iterate through the linked list
    current = head.next
    
    # Loop until there are no more nodes in the linked list
    while current:
        # Get the front node from the queue
        parent = queue.popleft()
        
        # Create the left child
        left_child = TreeNode(current.data)
        queue.append(left_child)
        parent.left = left_child
        current = current.next
        
        # Create the right child if there are more nodes
        if current:
            right_child = TreeNode(current.data)
            queue.append(right_child)
            parent.right = right_child
            current = current.next
    
    return root

def printLevelOrder(root):
    if not root:
        return
    
    queue = deque([root])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(str(current.data))
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    print(" ".join(result))

# Example usage
if __name__ == "__main__":
    # Construct the linked list
    data = [12, 34, 22, 41, 4, 7, 27, 6, 8, 42, 23, 31, 19, 7, 11, 21, 24, 36, 46, 24, 28, 44, 6, 14, 20, 20, 22, 4, 8, 32, 38, 7, 38, 31, 5, 3, 38, 30, 28, 46, 31, 11, 37, 6, 4, 26, 35, 46, 32, 18, 5, 7, 5, 20, 9, 44, 42, 2, 25, 40, 9, 39, 42, 28, 43, 15, 9, 22, 37, 5, 16, 18, 44, 29, 23, 10, 17, 38, 41, 21, 32, 31, 14]
    head = ListNode(data[0])
    current = head
    for value in data[1:]:
        current.next = ListNode(value)
        current = current.next
    
    # Convert linked list to binary tree
    root = convert(head)
    
    # Print level order traversal of the binary tree
    printLevelOrder(root)
