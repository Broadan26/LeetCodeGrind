# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: # No tree exists
            return 0

        count = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            count += 1
            left = False
            right = False
            if node.left:
                queue.append(node.left)
                left = True
            if node.right:
                queue.append(node.right)
                right = True
            
            if not right and not left:
                count += len(queue)
                queue = None
        return count