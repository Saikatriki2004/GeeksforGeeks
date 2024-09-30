class Solution:
    def inorder(self, root, res):
        if root is None:
            return
        # Traverse the left subtree
        self.inorder(root.left, res)
        # Visit the node
        res.append(root.data)
        # Traverse the right subtree
        self.inorder(root.right, res)

    def merge(self, root1, root2):
        # Perform inorder traversal of both trees to get sorted lists
        list1, list2 = [], []
        self.inorder(root1, list1)
        self.inorder(root2, list2)

        # Merge the two sorted lists
        merged_list = self.mergeSortedLists(list1, list2)
        return merged_list

    def mergeSortedLists(self, list1, list2):
        i, j = 0, 0
        merged = []
        
        # Merge the two sorted lists
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Append any remaining elements
        while i < len(list1):
            merged.append(list1[i])
            i += 1
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        
        return merged
BST1:
       5
     /   \
    3     6
   / \
  2   4  

BST2:
        2
      /   \
     1     3
            \
             7
            /
           6
