class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        if not head:  # If the list is empty, return two empty lists
            return [None, None]

        # Initialize two heads for the two sublists
        head1 = head
        head2 = head.next

        # Initialize pointers to build the two sublists
        current1 = head1
        current2 = head2

        # Traverse the original list to split nodes alternately
        current = head.next.next  # Start from the third node
        index = 0  # Use index to alternate between two lists

        while current:
            if index % 2 == 0:
                current1.next = current
                current1 = current1.next
            else:
                current2.next = current
                current2 = current2.next
            current = current.next
            index += 1

        # Set the last node of both sublists to None
        current1.next = None
        if current2:
            current2.next = None

        return [head1, head2]

# Helper function to print linked lists for testing
def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Example usage:
# Create a linked list: 0 -> 1 -> 0 -> 1 -> 0 -> 1
head = Node(0)
head.next = Node(1)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
head.next.next.next.next.next = Node(1)

solution = Solution()
result = solution.alternatingSplitList(head)

# Print the two resulting linked lists
printList(result[0])  # Output: 0 -> 0 -> 0 -> None
printList(result[1])  # Output: 1 -> 1 -> 1 -> None
