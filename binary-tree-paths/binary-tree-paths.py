# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        Given the root of a binary tree, returns all the root-to-leaf paths in any order
        '''
        paths = []
        self.buildPath(root, '', paths)
        return paths
    
    def buildPath(self, root: TreeNode, path: str, paths: list[str]):
        '''
        Builds the paths for the binaryTreePaths function
        '''
        if root is None:
            return
        if root.left is None and root.right is None:
            path += str(root.val)
            paths.append(path)
        else:
            path += str(root.val) + '->'
        self.buildPath(root.left, path, paths)
        self.buildPath(root.right, path, paths)