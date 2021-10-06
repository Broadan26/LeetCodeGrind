# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.find_sum(root, 0)
        
    def find_sum(self, root: TreeNode, num: int) -> int:
        if not root:
            return 0
        num *= 10
        num += root.val
        if not root.left and not root.right:
            return num
        else:
            return self.find_sum(root.left, num) + self.find_sum(root.right, num)