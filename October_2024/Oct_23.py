# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Initialize two pointers
        fast = slow = head

        # Move 'fast' n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both 'fast' and 'slow' until 'fast' reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Calculate the sum of the last n nodes
        total_sum = 0
        while slow:
            total_sum += slow.data
            slow = slow.next

        return total_sum
