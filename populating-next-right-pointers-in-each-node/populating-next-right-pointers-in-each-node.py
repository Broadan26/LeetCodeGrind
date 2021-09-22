"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: #Tree does not exist
            return None
        
        current_level = 1
        next_level = 0
        queue = [root]
        while queue: # BFS
            node = queue.pop(0)
            if node.left: # Add left child if it exists
                queue.append(node.left)
                next_level += 1
            if node.right: # Add right child if it exists
                queue.append(node.right)
                next_level += 1
            if current_level != 1: # Not on edge of tree level
                node.next = queue[0]

            current_level -= 1
            if current_level == 0: #Moved to next level of tree
                current_level = next_level
                next_level = 0
        
        return root