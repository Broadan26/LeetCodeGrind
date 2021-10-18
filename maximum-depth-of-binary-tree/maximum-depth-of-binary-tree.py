# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, 0)
    
    def dfs(self, root: TreeNode, depth: int) -> int:
        if not root:
            return depth
        depth += 1
        return max(self.dfs(root.left, depth), self.dfs(root.right, depth))