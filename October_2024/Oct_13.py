class Solution:
    def deleteAlt(self, head):
        # If the list is empty or has only one node, no deletion is needed
        if not head or not head.next:
            return head

        # Initialize the current node to the head
        current = head

        # Traverse the list while there is a next node to process
        while current and current.next:
            # Skip the next node by pointing to the next of next
            current.next = current.next.next

            # Move the current pointer to the next node (after skipping one)
            current = current.next

        return head
