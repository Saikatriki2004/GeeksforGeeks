class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # Find the end of the first half and the start of the second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether the list is palindrome
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.data != second_position.data:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
