class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
 class Solution:
    def removeAllDuplicates(self, head):
        if not head:
            return None
        
        # Dummy node to handle edge cases
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        
        # Iterate through the list
        while head:
            # If it's the start of duplicates sublist, skip all duplicates
            if head.next and head.data == head.next.data:
                # Move till the end of duplicates sublist
                while head.next and head.data == head.next.data:
                    head = head.next
                # Skip all duplicates
                prev.next = head.next
            else:
                # Otherwise, move predecessor
                prev = prev.next
            # Move forward
            head = head.next
        
        return dummy.next
      
# Example usage:
sol = Solution()
input_list = list_to_linked_list([23, 28, 28, 35, 49, 49, 53, 53])
output_list = sol.removeAllDuplicates(input_list)
print(linked_list_to_list(output_list))  # Output: [23, 35]

input_list = list_to_linked_list([11, 11, 11, 11, 75, 75])
output_list = sol.removeAllDuplicates(input_list)
print(linked_list_to_list(output_list))  # Output: []
      
      
