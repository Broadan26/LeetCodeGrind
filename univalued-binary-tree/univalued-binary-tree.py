# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        '''
        Determines if the given binary tree only contains a single value
        Returns true if it does, otherwise false
        '''
        c1 = True
        c2 = True
        if root is not None:
            if root.left:
                if root.left.val == root.val:
                    c1 = self.isUnivalTree(root.left)
                else:
                    c1 = False
            if root.right:
                if root.right.val == root.val:
                    c2 = self.isUnivalTree(root.right)
                else:
                    c2 = False
        return c1 and c2