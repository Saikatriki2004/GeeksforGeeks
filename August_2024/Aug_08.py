#Sum Tree:
class Solution:
    def is_sum_tree(self, node):
        # Helper function to check if the tree is a sum tree
        def check_sum_tree(root):
            # Base cases
            if root is None:
                return True, 0
            if root.left is None and root.right is None:
                return True, root.data
            
            # Recursively check left and right subtrees
            left_is_sum_tree, left_sum = check_sum_tree(root.left)
            right_is_sum_tree, right_sum = check_sum_tree(root.right)
            
            # Check if current node satisfies the Sum Tree property
            if left_is_sum_tree and right_is_sum_tree and root.data == left_sum + right_sum:
                return True, root.data + left_sum + right_sum
            else:
                return False, 0
        
        is_sum_tree, _ = check_sum_tree(node)
        return is_sum_tree
