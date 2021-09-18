# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if root is None: #No nodes
            return answer
        
        queue = []
        queue.append(root)
        temp = []
        current_level = 1
        next_level = 0
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                next_level += 1
                queue.append(node.left)
            if node.right is not None:
                next_level += 1
                queue.append(node.right)
            current_level -= 1
            temp.append(node.val)
            if current_level == 0:
                current_level = next_level
                next_level = 0
                answer.insert(0, temp)
                temp = []
        return answer