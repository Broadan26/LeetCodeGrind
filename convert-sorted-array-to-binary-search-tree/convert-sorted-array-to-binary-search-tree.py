# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BST(self, nums: list[int], l: int, r: int) -> TreeNode:
        '''
        Performs the recursive D&C to create the balanced BST
        '''
        root = None
        if l <= r:
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = self.BST(nums, l, mid - 1)
            root.right = self.BST(nums, mid + 1, r)
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        Takes a sorted array and converts it to a balanced binary tree
        Returns the root of a balanced binary tree
        '''
        return self.BST(nums, 0, len(nums) - 1)