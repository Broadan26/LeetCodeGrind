class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        Given a matrix of m x n dimension, performs adjustments to matrix if matrix has zeroes
        Returns nothing, performs changes in place
        '''
        change_first_col = False
        for row in range(len(matrix)): #Find which rows/cols need to be set to 0's
            if matrix[row][0] == 0:
                change_first_col = True
            for col in range(1, len(matrix[0])): 
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, len(matrix)): #Change everything except first row/col to 0's
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0: #Change first row/col to 0
            matrix[0] = [0] * len(matrix[0]) #Change row 0 to all 0's

        if change_first_col: #Change col 0 to all 0's
            for row in range(0, len(matrix)):
                matrix[row][0] = 0