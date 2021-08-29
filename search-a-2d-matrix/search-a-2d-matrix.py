class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Given a 2D list and a targeted value, returns if the target is in the array
        Returns true if in the matrix, returns false otherwise
        '''
        for row in range(0, len(matrix), 1):
            if row == (len(matrix) - 1) or (matrix[row][0] <= target and matrix[row+1][0] > target):
                for col in range(0, len(matrix[row]), 1):
                    if matrix[row][col] == target:
                        return True
                break
        return False