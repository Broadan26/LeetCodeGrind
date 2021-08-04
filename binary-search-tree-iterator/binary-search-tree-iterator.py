# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.buildStack(self.root)

    def next(self) -> int:
        '''
        Collects the value in the current node and moves the pointer
        Returns the value in the current node
        '''
        rootval = self.stack.pop()
        if rootval.right:
            self.buildStack(rootval.right)
        return rootval.val

    def hasNext(self) -> bool:
        '''
        Checks if an element remains to right of the current pointer
        Returns true if it exists, false otherwise
        '''
        if self.stack:
            return True
        else:
            return False
        
    def buildStack(self, root: TreeNode):
        '''
        Builds the stack to traverse the BST
        '''
        while root:
            self.stack.append(root)
            if root.left:
                root = root.left
            else:
                root = None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()