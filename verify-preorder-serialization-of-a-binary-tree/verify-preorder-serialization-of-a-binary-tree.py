class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        '''
        Given a string of numbers and pounds, returns if the string is a valid preorder BST
        Returns true if it is, false otherwise
        '''
        preorder = preorder.split(',') #Iterate just useful chars
        if preorder[0] == '#': #Tree should be empty
            return len(preorder) == 1

        stack = [preorder[0]]
        for i in range(1, len(preorder)): #Iterate the tree
            if preorder[i] != '#':
                stack.append(preorder[i]) #Add the subtree root
            else:
                if not stack: #Stack is emptied
                    return i == len(preorder) - 1
                stack.pop() #Pop the parent once #'s found
        return False