# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        Inverts a binary tree along the y-axis
        Returns the inverted binary tree root node
        '''
        node = None
        if root:
            node = TreeNode(root.val)
            node.left = self.invertTree(root.right)
            node.right = self.invertTree(root.left)
        return node