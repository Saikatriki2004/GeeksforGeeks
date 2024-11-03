class Solution:
    def isLengthEven(self, head):
        # Initialize a counter
        count = 0
        # Traverse the list
        current = head
        while current:
            count += 1
            current = current.next
        # Check if the count is even or odd
        return count % 2 == 0
