"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = [root]
        curr_level = 1
        next_level = 0
        depth = 0
        while queue:
            node = queue.pop(0)
            curr_level -= 1
            for child in node.children:
                queue.append(child)
                next_level += 1
            if curr_level == 0:
                curr_level = next_level
                next_level = 0
                depth += 1
        return depth