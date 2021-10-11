# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0] # Create mutable object/accessible via assignment
        self.dfs(root, diameter)
        return diameter[0]
    
    def dfs(self, root: TreeNode, diameter: list[int]) -> int:
        if not root:
            return 0
        lh = self.dfs(root.left, diameter)
        rh = self.dfs(root.right, diameter)
        diameter[0] = max(diameter[0], lh+rh)
        return 1 + max(lh, rh)