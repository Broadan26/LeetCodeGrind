# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Given a tree comprised of 0's and 1's, determines which subtrees to keep
        Keeps subtrees if they contain a 1 and removes subtrees without 1's
        Returns the root of the original tree
        '''
        keep = self.helper(root)
        return root if keep else None
        
    def helper(self, root: TreeNode) -> bool:
        if root is None: #Node does not exist
            return False

        left = self.helper(root.left) #Check if subtrees contain 1's
        right = self.helper(root.right)

        if not left: #Left contains no ones
            root.left = None
        if not right: #Right contains no ones
            root.right = None
        return left or right or root.val