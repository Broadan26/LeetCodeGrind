# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node_list = self.dfs(root, [])
        new_tree = node_list[0]
        new_tree.left = None
        it = new_tree
        for node in range(1, len(node_list)):
            it.right = node_list[node]
            node_list[node].left = None
            it = it.right
        return new_tree
            
    
    def dfs(self, root: TreeNode, node_list: list[TreeNode]) -> list[TreeNode]:
        if not root:
            return []
        self.dfs(root.left, node_list)
        node_list.append(root)
        self.dfs(root.right, node_list)
        return node_list