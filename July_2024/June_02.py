class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def compute(head):
    # Step 1: Concatenate all strings in the linked list
    combined_string = ""
    current = head
    while current:
        combined_string += current.data
        current = current.next
    
    # Step 2: Check if the concatenated string is a palindrome
    return combined_string == combined_string[::-1]

# Helper function to create a linked list from a list of strings
def create_linked_list(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        current.next = Node(element)
        current = current.next
    return head

# Example usage:
# Case 1: Palindrome linked list
elements1 = ["abc", "dd", "cba"]
head1 = create_linked_list(elements1)
print(compute(head1))  # Output: True

# Case 2: Non-palindrome linked list
elements2 = ["abc", "d", "cba"]
head2 = create_linked_list(elements2)
print(compute(head2))  # Output: False
