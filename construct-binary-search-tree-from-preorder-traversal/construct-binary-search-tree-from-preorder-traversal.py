# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        Creates a BST from a list ordered by preorder
        Returns the root of the created tree
        Preorder = Root, left, right
        '''
        root = TreeNode(preorder.pop(0)) #Remove first element from list
        if len(preorder) != 0 and preorder[0] < root.val: #Build left tree if element exists & is < root
            root.left = self.buildLeftTree(preorder, root.val)
        if len(preorder) != 0: #Build right tree if element exists
            root.right = self.buildRightTree(preorder)
        return root
    
    def buildLeftTree(self, preorder: list[int], parentVal: int) -> TreeNode:
        '''
        Handles any left subtree with a max restriction
        '''
        root = TreeNode(preorder.pop(0))
        if len(preorder) != 0 and preorder[0] < root.val: #Build left tree if element exists & is < root
            root.left = self.buildLeftTree(preorder, root.val)
        if len(preorder) != 0 and preorder[0] < parentVal: #Build right tree if element exists & is < parent
            root.right = self.buildLeftTree(preorder, parentVal)
        return root
    
    def buildRightTree(self, preorder: list[int]) -> TreeNode:
        '''
        Handles any right subtree without a max restriction
        '''
        root = TreeNode(preorder.pop(0))
        if len(preorder) != 0 and preorder[0] < root.val: #Build left tree if element exists & is < root
            root.left = self.buildLeftTree(preorder, root.val)
        if len(preorder) != 0: #Build right subtree without restrictions
            root.right = self.buildRightTree(preorder)
        return root