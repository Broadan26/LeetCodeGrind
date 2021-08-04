# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Returns the preorder traversal of a binary tree graph in a list
        '''
        preorder = []
        if root:
            preorder = self.createList(root, preorder)
        return preorder
    
    def createList(self, root: TreeNode, preorder: list) -> list:
        if root:
            preorder.append(root.val)
            preorder = self.createList(root.left, preorder)
            preorder = self.createList(root.right, preorder)
        return preorder