class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        # Step 1: Create the new node to be inserted
        new_node = Node(x)
        
        # Step 2: Handle the case where the list is empty
        if head is None:
            return new_node
        
        # Step 3: Insert at the beginning if x is smaller than the head's data
        if x < head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        
        # Step 4: Traverse the list to find the insertion point
        current = head
        while current.next and current.next.data < x:
            current = current.next
        
        # Step 5: Insert the new node after the current node
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
        return head
