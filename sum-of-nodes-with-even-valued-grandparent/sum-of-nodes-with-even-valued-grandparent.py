# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        '''
        Given a binary tree, calculates the sum of the grandchildren of even nodes
        Returns the sum as an int
        '''
        even_grandparents_sum = 0
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
                if node.val % 2 == 0:
                    even_grandparents_sum += self.checkGrandChildren(node.left)
            if node.right is not None:
                queue.append(node.right)
                if node.val % 2 == 0:
                    even_grandparents_sum += self.checkGrandChildren(node.right)
        return even_grandparents_sum

    def checkGrandChildren(self, node: TreeNode) -> int:
        temp_sum = 0
        if node.left is not None:
            temp_sum += node.left.val
        if node.right is not None:
            temp_sum += node.right.val
        return temp_sum