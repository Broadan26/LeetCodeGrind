# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        node_list = self.collect_nodes(root) # Collect node values
        node_list = sorted(node_list) # Sort the list
        root = self.create_bst(node_list, 0, len(node_list)-1) # Create a balanced BST
        return root
    
    def collect_nodes(self, root: TreeNode) -> list[int]:
        '''
        BFS collection of node values
        '''
        queue = []
        queue.append(root)
        node_list = []
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node_list.append(node.val)
        return node_list
    
    def create_bst(self, node_list: list[int], lo: int, hi: int) -> TreeNode:
        if lo > hi: #Base Case
            return None
        mid = lo + (hi-lo) // 2
        root = TreeNode(node_list[mid])
        root.left = self.create_bst(node_list, lo, mid-1)
        root.right = self.create_bst(node_list, mid+1, hi)

        return root