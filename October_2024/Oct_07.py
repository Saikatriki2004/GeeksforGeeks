#User function Template for python3
def insert(head, data):
    n = Node(data)
    n.npx = head
    head = n
    return head
    
def getList(head):
    lx = []
    
    temp = head
    
    while temp != None:
        lx.append(temp.data)
        temp = temp.npx
    
    return lx
