# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        Given a value, inserts the value into the tree.
        Returns the root of the tree the val is inserted into
        '''
        if root is None: #Tree is empty, return new tree
            return TreeNode(val)

        iter = root
        while True:
            if iter.left is None and iter.val > val: #No node, val < node.val
                iter.left = TreeNode(val)
                break
            elif iter.right is None and iter.val < val: #No node, val > node.val
                iter.right = TreeNode(val)
                break
            elif iter.left and iter.val > val: #Node exists, val < node.val
                iter = iter.left
            else: #Node exists, val > node.val
                iter = iter.right
        return root