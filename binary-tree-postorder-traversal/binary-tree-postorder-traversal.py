# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Returns the postorder traversal of a binary tree graph in a list
        '''
        postorder = []
        if root:
            postorder = self.createList(root, postorder)
        return postorder
    
    def createList(self, root: TreeNode, postorder: list) -> list:
        if root:
            postorder = self.createList(root.left, postorder)
            postorder = self.createList(root.right, postorder)
            postorder.append(root.val)
        return postorder