# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root or not subRoot: return False
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val == subRoot.val:
                if self.check_subtree(node, subRoot): return True
        return False
                
    def check_subtree(self, root: TreeNode, sub_root: TreeNode) -> bool:
        root_q = [root]
        subroot_q = [sub_root]
        while root_q and subroot_q:
            root_node = root_q.pop(0)
            sub_node = subroot_q.pop(0)
            
            if root_node.val != sub_node.val: # Not a subtree
                return False
            
            if root_node.left and sub_node.left: # Check left
                root_q.append(root_node.left)
                subroot_q.append(sub_node.left)
            elif root_node.left or sub_node.left: return False
                
            if root_node.right and sub_node.right: # Check right
                root_q.append(root_node.right)
                subroot_q.append(sub_node.right)
            elif root_node.right or sub_node.right: return False
                
        return len(root_q) == len(subroot_q)