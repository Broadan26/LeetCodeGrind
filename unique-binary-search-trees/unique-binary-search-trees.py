class Solution:
    def numTrees(self, n: int) -> int:
        '''
        Calculates the number of structurally unique BSTs given the number of nodes in the tree
        Returns the number of unique trees
        '''
        return int(self.factorial(2 * n) / (self.factorial(n + 1) * self.factorial(n)))
    
    def factorial(self, n: int) -> int:
        sum = 1
        while n > 0:
            sum *= n
            n -= 1
        return sum