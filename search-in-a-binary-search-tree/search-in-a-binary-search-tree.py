# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''
        Searches a given BST for a particular value in the node
        Returns the subtree of the requested node
        '''
        node = None
        if root is None:
            node = None
        elif root.val == val:
            node = root
        elif root.val > val:
            node = self.searchBST(root.left, val)
        elif root.val < val:
            node = self.searchBST(root.right, val)
        return node