# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def dfs(self, root: TreeNode, target: int, current) -> int:
        if not root:
            return 0
        count = 0
        current = root.val + current
        if current == target:
            count += 1
        return count + self.dfs(root.left, target, current) + self.dfs(root.right, target, current)