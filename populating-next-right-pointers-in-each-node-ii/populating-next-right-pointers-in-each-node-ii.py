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
        if root is None: # Handle case of no tree
            return None
        
        current_level = 1 # Root has 1 node on its level
        next_level = 0 # Determine how many nodes in next level
        queue = [root] # Initialize queue
        while queue: # BFS
            node = queue.pop(0)
            if node.left: # Node has a left child
                next_level += 1
                queue.append(node.left)
            if node.right: # Node has a right child
                next_level += 1
                queue.append(node.right)
            if current_level != 1:
                node.next = queue[0]
                
            current_level -= 1
            if current_level == 0:
                current_level = next_level
                next_level = 0
        
        return root