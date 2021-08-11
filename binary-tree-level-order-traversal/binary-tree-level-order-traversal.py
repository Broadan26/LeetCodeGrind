# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Returns the level order traversal of a binary tree's nodes
        '''
        answer = []
        if root is not None:
            self.levelOrderHelper(root, 0, answer)
        return answer
    
    def levelOrderHelper(self, root: TreeNode, level: int, answer: list[int]):
        if level == len(answer): #Create a new level
            answer.append([])
        answer[level].append(root.val) #Append the node at that level's value
        if root.left is not None: #Left node exists
            self.levelOrderHelper(root.left, level + 1, answer)
        if root.right is not None: #Right node exists
            self.levelOrderHelper(root.right, level + 1, answer)