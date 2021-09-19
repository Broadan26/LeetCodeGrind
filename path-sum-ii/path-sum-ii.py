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
        if root is None: # Nothing to be done
            return answer

        def dfs(node: TreeNode, path: list[int], currentSum: int):
            if not node:
                return 0
            if node.left == None and node.right == None and currentSum == node.val:
                path.append(node.val)
                answer.append(path)
            dfs(node.left, path + [node.val], currentSum - node.val)
            dfs(node.right, path + [node.val], currentSum - node.val)

        dfs(root, [], targetSum)
        return answer