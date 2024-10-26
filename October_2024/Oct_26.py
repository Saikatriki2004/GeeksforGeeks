class Solution:
    def count(self, head, key):
        # Initialize the counter
        count = 0
        # Traverse the linked list
        current = head
        while current:
            # If the current node's data matches the key, increment the counter
            if current.data == key:
                count += 1
            # Move to the next node
            current = current.next
        return count
