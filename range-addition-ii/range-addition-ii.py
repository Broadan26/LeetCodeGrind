class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        '''
        Given the dimensions of a 2D list and operations applied to the 2D list
        Finds the number of largest values after performing operations based on the ops list
        Returns the number of largest values as an int
        '''
        if len(ops) == 0:
            return m * n

        op1 = float('inf')
        op2 = float('inf')
        for op in ops:
            if op[0] < op1:
                op1 = op[0]
            if op[1] < op2:
                op2 = op[1]

        return op1 * op2