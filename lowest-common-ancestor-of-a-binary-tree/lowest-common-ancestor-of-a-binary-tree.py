# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def postorderDFS(node: TreeNode) -> list[TreeNode]: # Post Order
            if node is None: # Node is empty
                return False
            left = postorderDFS(node.left) # Iterate left
            right = postorderDFS(node.right) # Iterate right
            mid = node == p or node == q # Check root

            if mid + left + right >= 2: # Check if subtree contains all nodes
                self.answer = node
            return mid or left or right # Return if at least p or q node exists
        
        postorderDFS(root)
        return self.answer