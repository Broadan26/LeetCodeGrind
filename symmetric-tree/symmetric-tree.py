# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        Determines if the binary tree is a mirror of itself
        Returns true if it is, otherwise false
        '''
        return self.checkMirror(root, root)
    
    def checkMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None: #'None' is symmetric
            return True
        if root1 is not None and root2 is not None: #Something exists
            if root1.val == root2.val: #Except root, check symmetry
                return self.checkMirror(root1.right, root2.left) and self.checkMirror(root1.left, root2.right)
        return False