# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Initialize current pointers for both lists
    current1 = head1
    current2 = head2
    
    # Traverse both lists
    while current1 is not None and current2 is not None:
        # If data in current nodes does not match, return false
        if current1.data != current2.data:
            return False
        
        # Move to the next nodes in both lists
        current1 = current1.next
        current2 = current2.next
    
    # If either list has remaining nodes, they are not identical
    if current1 is not None or current2 is not None:
        return False
    
    # If we reached here, both lists are identical
    return True

# Helper function to create linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for item in lst[1:]:
        current.next = Node(item)
        current = current.next
    return head


# Example usage:
head1 = create_linked_list([1, 2, 3, 4, 5, 6])
head2 = create_linked_list([99, 59, 42, 20])
print(areIdentical(head1, head2))  # Output: False

head3 = create_linked_list([1, 2, 3, 4, 5])
head4 = create_linked_list([1, 2, 3, 4, 5])
print(areIdentical(head3, head4))  # Output: True
