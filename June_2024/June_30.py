class Solution:
    def delete_node(self, head, x):
        # If the list is empty or position is invalid
        if not head or x <= 0:
            return head
        
        current = head

        # If head needs to be removed
        if x == 1:
            head = current.next
            if head:
                head.prev = None
            return head

        # Traverse to the node to be deleted
        for _ in range(x - 1):
            current = current.next
            if not current:
                return head
        
        # If the node to be deleted is the last node
        if not current.next:
            current.prev.next = None
        else:
            # Remove the node by adjusting the pointers
            current.prev.next = current.next
            current.next.prev = current.prev
        
        return head


# Example usage:
sol = Solution()
head1 = create_doubly_linked_list([1, 3, 4])
head1 = sol.delete_node(head1, 3)
print_doubly_linked_list(head1)  # Output: 1 3

head2 = create_doubly_linked_list([1, 5, 2, 9])
head2 = sol.delete_node(head2, 1)
print_doubly_linked_list(head2)  # Output: 5 2 9
