class Solution:
    def createTree(self, parent):
        n = len(parent)
        nodes = [Node(i) for i in range(n)]
        root = None

        for i in range(n):
            if parent[i] == -1:
                root = nodes[i]
            else:
                p = parent[i]
                if nodes[p].left is None:
                    nodes[p].left = nodes[i]
                else:
                    nodes[p].right = nodes[i]
                    
        return root
      # Example usage
def printLevelOrder(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()

sol = Solution()
parent = [-1, 0, 0, 1, 1, 3, 5]
root = sol.createTree(parent)
printLevelOrder(root)  # Output should be: 0 1 2 3 4 5 6

parent = [2, 0, -1]
root = sol.createTree(parent)
printLevelOrder(root)  # Output should be: 2 0 1
