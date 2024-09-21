class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

class Solution:
    def copyList(self, head):
        if not head:
            return None
        
        # Step 1: Create new nodes interweaved with the original nodes
        current = head
        while current:
            new_node = Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Copy random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the two interweaved lists
        current = head
        copy_head = head.next
        copy_current = copy_head
        
        while current:
            current.next = current.next.next
            if copy_current.next:
                copy_current.next = copy_current.next.next
            current = current.next
            copy_current = copy_current.next
        
        return copy_head
