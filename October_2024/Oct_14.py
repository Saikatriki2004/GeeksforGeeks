class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # Initialize count
        count = 0
        current = head

        # Traverse the linked list
        while current is not None:
            count += 1
            current = current.next

        return count
