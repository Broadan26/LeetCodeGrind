# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: # No tree exists
            return False
        
        queue = [root] # Setup queue
        nodes_on_level = 1 # Track nodes per level
        nodes_next_level = 0
        
        current_depth = 0 # Track depths
        depth_x = -1
        depth_y = -2
        while queue:
            node = queue.pop(0) # Pop the queue and decrement queue
            nodes_on_level -= 1
            if node.left: # Check left child
                queue.append(node.left)
                nodes_next_level += 1
            if node.right: # Check right child
                queue.append(node.right)
                nodes_next_level += 1
                
            if node.left and node.right: # Check for parent
                if node.left.val == x and node.right.val == y: return False
                if node.left.val == y and node.right.val == x: return False
                
            if node.val == x: # Check for x
                depth_x = current_depth
            if node.val == y: # Check for y
                depth_y = current_depth
                
            if nodes_on_level == 0: # Reached end of current level
                current_depth += 1
                nodes_on_level = nodes_next_level
                nodes_next_level = 0
        return depth_x == depth_y