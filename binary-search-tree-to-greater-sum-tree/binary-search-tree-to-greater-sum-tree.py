# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        '''
        Given a BST, calculates the sum of every node from right to left and inserts it into the corresponding node
        Returns the original tree with the updated node values
        '''
        self.sum = 0
        self.reverse_order(root)
        return root

    def reverse_order(self, root: TreeNode) -> int:
        if root is None: #Base Case
            return 0
        self.reverse_order(root.right) #Right
        self.sum = self.sum + root.val #Root
        root.val = self.sum
        self.reverse_order(root.left) #Left