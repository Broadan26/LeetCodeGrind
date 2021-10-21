# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0 or n < 0: # No trees possible
            return []
        if n == 1: # Case where tree has 1 node
            return [TreeNode(0)]
        
        answer = [] # List to store potential trees
        
        for i in range(1, n, 2):
            left_subtree = self.allPossibleFBT(i) # Build left subtrees
            right_subtree = self.allPossibleFBT(n-i-1) # Build right subtrees
            
            for l_node in left_subtree: # Run through left subtrees
                for r_node in right_subtree: # Run through right subtrees
                    root = TreeNode(0) # Build the tree
                    root.left = l_node
                    root.right = r_node
                    answer.append(root) # Append final trees
        return answer