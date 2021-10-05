# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        min_depth = 1
        current_level, next_level = 1, 0
        queue = [root]
        while queue: # Run thru tree
            node = queue.pop(0)
            current_level -= 1
            if not node.left and not node.right: # Check if leaf node
                return min_depth
            if node.left: # Check left
                queue.append(node.left)
                next_level += 1
            if node.right: # Check right
                queue.append(node.right)
                next_level += 1
            if current_level == 0:
                min_depth += 1
                current_level, next_level = next_level, 0