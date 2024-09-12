# Node definition
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Should return data of middle node. If linked list is empty, return -1
    def findMid(self, head):
        # Edge case: if the linked list is empty
        if head is None:
            return -1
        
        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        # Traverse the list. Fast moves twice as fast as slow
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # Slow pointer will now be pointing at the middle node
        return slow.data
