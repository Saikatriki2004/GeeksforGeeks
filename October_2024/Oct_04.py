class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        # If the list is empty
        if not head:
            return None
        
        # If the node to be deleted is the only node in the circular list
        if head.data == key and head.next == head:
            return None
        
        # Initialize previous and current pointers
        prev = None
        curr = head
        
        # If the head is to be deleted, we need to handle separately
        if head.data == key:
            # Find the last node (node pointing to head)
            temp = head
            while temp.next != head:
                temp = temp.next
            # Last node found, now remove head and set new head
            temp.next = head.next
            head = head.next
            return head
        
        # Otherwise, we search for the key in the list
        while curr.next != head:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
        
        # If we found the node with the key, delete it
        if curr.data == key:
            prev.next = curr.next
        
        return head

    # Function to reverse a circular linked list
    def reverse(self, head):
        if not head or head.next == head:
            return head
        
        prev = None
        curr = head
        next_node = None
        first_node = head
        
        # Reverse the links between nodes
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == head:
                break
        
        # Now fix the head and the last node (which was the original head)
        first_node.next = prev
        head = prev
        
        return head
