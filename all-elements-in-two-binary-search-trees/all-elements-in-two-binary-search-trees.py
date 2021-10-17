# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1 = self.dfs(root1, []) # DFS tree1
        tree2 = self.dfs(root2, []) # DFS tree2
        merged_list = tree1 + tree2
        merged_list.sort()
        return merged_list
    
    def dfs(self, root: TreeNode, tree_list: list[int]) -> list[int]:
        if not root:
            return []
        self.dfs(root.left, tree_list)
        tree_list.append(root.val)
        self.dfs(root.right, tree_list)
        return tree_list