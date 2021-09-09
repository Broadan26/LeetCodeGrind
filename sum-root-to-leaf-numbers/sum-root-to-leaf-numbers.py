# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.the_sum = 0
    
    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.the_sum
        
    def dfs(self, root: TreeNode, curr: int) -> int:
        curr = (curr * 10) + root.val 
        if root.left is None and root.right is None: #No children exist
            self.the_sum += curr
            print(curr)
        else: #A child node exists
            if root.left is not None:
                self.dfs(root.left, curr)
            if root.right is not None:
                self.dfs(root.right, curr)