# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Creates a maximum binary tree split at each level
        Returns the root node
        '''
        if len(nums) == 0:
            return None
        maxVal = float('-inf')
        loc = -1
        for i in range(len(nums)): #Find the max value and its location
            if nums[i] > maxVal:
                maxVal = nums[i]
                loc = i
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[0:loc])
        root.right = self.constructMaximumBinaryTree(nums[loc+1:len(nums)])
        return root