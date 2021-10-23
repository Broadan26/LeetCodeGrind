# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = self.dfs(root, root.val)
        return good
    
    def dfs(self, root: TreeNode, prev_max: int) -> int:
        if not root:
            return 0
        curr_max = max(prev_max, root.val)
        if root.val >= curr_max:
            return 1 + self.dfs(root.left, curr_max) + self.dfs(root.right, curr_max)
        else:
            return self.dfs(root.left, curr_max) + self.dfs(root.right, curr_max)