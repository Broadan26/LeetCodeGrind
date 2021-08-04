# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        '''
        Flattens a BST into a linked list where 'right' points to next element
        Modifies the BST in-place
        '''
        if not root:
            return None
        copyRoot = root
        while copyRoot:
            if copyRoot.left != None:
                leftNode = copyRoot.left
                temp = leftNode
                while temp.right:
                    temp = temp.right
                temp.right = copyRoot.right
                copyRoot.right = leftNode
                copyRoot.left = None
            copyRoot = copyRoot.right