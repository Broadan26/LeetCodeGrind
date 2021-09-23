# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: # No tree exists
            return None

        answer = [] # Answer to return
        current_level = 1 # Count nodes on current level
        next_level = 0 # Count nodes on next level
        queue = [root]
        while queue: # BFS
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                next_level += 1
            if node.right:
                queue.append(node.right)
                next_level += 1

            current_level -= 1
            if current_level == 0: # If end of current level, remember rightmost node
                answer.append(node.val)
                current_level = next_level
                next_level = 0
        return answer