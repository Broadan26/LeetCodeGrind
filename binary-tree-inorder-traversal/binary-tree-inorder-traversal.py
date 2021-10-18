# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        return self.dfs(root, [])
    
    def dfs(self, root: TreeNode, node_list: list[int]) -> list[int]:
        if not root:
            return []
        self.dfs(root.left, node_list)
        node_list.append(root.val)
        self.dfs(root.right, node_list)
        return node_list