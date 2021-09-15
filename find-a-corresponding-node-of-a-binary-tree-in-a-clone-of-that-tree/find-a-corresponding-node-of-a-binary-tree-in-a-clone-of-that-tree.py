# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        '''
        Given an original binary tree, a copy of that same binary tree and a target node
        Finds the location of the same node in the copy of the original binary tree
        Returns the node of the copied tree
        '''
        queue = []
        queue.append(cloned)
        while queue is not None:
            popped = queue.pop(0)
            if popped.val == target.val:
                return popped
            if popped.left is not None:
                queue.append(popped.left)
            if popped.right is not None:
                queue.append(popped.right)
        return None