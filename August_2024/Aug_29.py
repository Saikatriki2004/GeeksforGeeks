# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def countNodesInLoop(self, head: Node) -> int:
        slow = fast = head
        
        # Step 1: Detect loop using Floyd's Cycle-Finding Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, there's a loop
            if slow == fast:
                return self.getLoopLength(slow)
        
        # No loop found
        return 0
    
    def getLoopLength(self, node: Node) -> int:
        count = 1
        temp = node
        
        # Step 2: Calculate the length of the loop
        while temp.next != node:
            count += 1
            temp = temp.next
        
        return count

# Helper function to create a loop in the linked list
def createLinkedListWithLoop(arr, loop_start_index):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    loop_start_node = None
    
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
        if i == loop_start_index:
            loop_start_node = curr
    
    # Creating a loop if loop_start_index is valid
    if loop_start_node:
        curr.next = loop_start_node
    
    return head

# Test the code with example input
arr = [25, 14, 19, 33, 10, 21, 39, 90, 58, 45]
loop_start_index = 4  # Loop starts at index 4 (node with value 10)

head = createLinkedListWithLoop(arr, loop_start_index)
solution = Solution()
loop_length = solution.countNodesInLoop(head)
print(loop_length)  # Expected Output: 7
