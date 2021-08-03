# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''
        Determines if a route-to-leaf path contains the target sum
        Returns True if a route exists, false otherwise
        '''
        if root is None: #Root contains nothing
            return False
        if root.left is None and root.right is None: #Check if targetSum reached
            if targetSum == root.val:
                return True
        current = targetSum - root.val #Update target val
        return (self.hasPathSum(root.left, current) or self.hasPathSum(root.right, current)) #Recurse for result