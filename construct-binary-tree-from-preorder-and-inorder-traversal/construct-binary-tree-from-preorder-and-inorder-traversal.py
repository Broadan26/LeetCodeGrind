# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0)) # Find the root of subtree
            root = TreeNode(inorder[index]) # Create the root node
            root.left = self.buildTree(preorder, inorder[0:index]) # Slice inorder, attach subtrees
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root