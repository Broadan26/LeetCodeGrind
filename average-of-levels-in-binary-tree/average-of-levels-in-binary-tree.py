# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        if not root: # No tree exists
            return answer

        queue = [root]
        current_level, next_level, nodes_on_level = 1, 0, 1
        running_sum = 0
        while queue: # Run through tree
            current_level -= 1
            node = queue.pop(0)
            running_sum += node.val
            if node.left: # Check left node
                queue.append(node.left)
                next_level += 1
            if node.right: # Check right node
                queue.append(node.right)
                next_level += 1
            if current_level == 0: # Moved to next level
                answer.append(running_sum / nodes_on_level)
                running_sum, nodes_on_level = 0, next_level
                current_level, next_level  = next_level, 0
        return answer