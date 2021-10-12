# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        '''Calculates the sum of left tree leaves'''
        the_sum = [0]
        if not root:
            return the_sum
        
        self.dfs(root, False, the_sum)
        return the_sum[0]
        
        
    def dfs(self, root: TreeNode, left: bool, the_sum: list[int]):
        '''DFS down the tree, calculating sum of left children'''
        if not root:
            return
        if not root.left and not root.right and left:
            the_sum[0] += root.val
        self.dfs(root.left, True, the_sum)
        self.dfs(root.right, False, the_sum)