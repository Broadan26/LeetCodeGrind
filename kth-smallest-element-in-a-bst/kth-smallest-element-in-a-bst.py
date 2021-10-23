# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: # Tree does not exist
            return -1
        node_list = self.dfs(root, [])
        return node_list[k-1]
    
    def dfs(self, root: TreeNode, node_list: list[int]) -> list[int]:
        if not root:
            return
        self.dfs(root.left, node_list)
        node_list.append(root.val)
        self.dfs(root.right, node_list)
        return node_list