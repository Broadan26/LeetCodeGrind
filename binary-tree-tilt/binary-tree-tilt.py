# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        '''DFS Approach to Find Tilt'''
        if not root: return 0
        tilt_sum = 0
        tilt_sum = abs(self.dfs(root.left) - self.dfs(root.right))
        return tilt_sum + self.findTilt(root.left) + self.findTilt(root.right)
    
    def dfs(self, root: TreeNode) -> int:
        if not root: return 0
        return root.val + self.dfs(root.left) + self.dfs(root.right)