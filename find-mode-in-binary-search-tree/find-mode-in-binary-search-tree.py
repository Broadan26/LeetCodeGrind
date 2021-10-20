# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root: # No tree exists
            return None
        mode_dict = {} # Track node counts
        queue = [root]
        while queue: # Basic BFS
            node = queue.pop(0)
            if node.left: # Check left
                queue.append(node.left)
            if node.right: # Check right
                queue.append(node.right)
            if node.val not in mode_dict: # Node not in dict
                mode_dict[node.val] = 1
            else: # Increment if in dict
                mode_dict[node.val] += 1
        return [key for key, val in mode_dict.items() if val == max(mode_dict.values())]