# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        current_level = 1
        next_level = depth = curr_sum = 0
        max_depth = max_sum = float('-inf')
        while queue:
            node = queue.pop(0)
            current_level -= 1
            curr_sum += node.val
            if node.left:
                queue.append(node.left)
                next_level += 1
            if node.right:
                queue.append(node.right)
                next_level += 1
                
            if current_level == 0:
                current_level = next_level
                next_level = 0
                depth += 1
                if curr_sum > max_sum:
                    max_sum, max_depth = curr_sum, depth
                curr_sum = 0
        return max_depth