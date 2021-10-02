# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        '''Swaps the two elements that are out of place'''
        if root is None:
            return None

        node_list = self.inorder(root, []) # Get sorted list
        first = second = None # Node pointers to swap
        for i in range(1, len(node_list)): # Find first out of place node
            if node_list[i].val < node_list[i-1].val: #Found out of place node
                print('swap')
                first = node_list[i-1]
                break
        for i in range(len(node_list)-2, -1, -1): # Find second out of place node
            if node_list[i].val > node_list[i+1].val:
                print('swap')
                second = node_list[i+1]
                break

        first.val, second.val = second.val, first.val # Swap values in-place
        
    def inorder(self, root: TreeNode, node_list: list[TreeNode]) -> list[TreeNode]:
        '''Returns a sorted list of treenodes'''
        if root is None:
            return node_list
        node_list = self.inorder(root.left, node_list)
        node_list.append(root)
        node_list = self.inorder(root.right, node_list)
        return node_list