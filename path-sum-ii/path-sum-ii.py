# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        Given a binary tree and a target sum, find paths root->leaf that equals the targetSum
        Returns a list of paths root->leaf as a list of lists
        '''
        answer = []
        if not root:
            return answer
		
        self.find_current_paths(root, targetSum, [], answer)
        return answer

    def find_current_paths(self, root: TreeNode, s: int, temp: list[int], answer: list[list[int]]):
        if not root:
            return
        
        temp.append(root.val)
        if root.val == s and not root.left and not root.right:
            answer.append(list(temp))
        else:
            self.find_current_paths(root.left, s-root.val, temp, answer)
            self.find_current_paths(root.right, s-root.val, temp, answer)
        del temp[-1]