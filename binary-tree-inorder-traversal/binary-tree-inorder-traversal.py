# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        if root:
            inorder = self.createList(root, inorder)
        return inorder
    def createList(self, root: TreeNode, inorder: list) -> list:
        if root:
            inorder = self.createList(root.left, inorder)
            inorder.append(root.val)
            inorder = self.createList(root.right, inorder)
        return inorder