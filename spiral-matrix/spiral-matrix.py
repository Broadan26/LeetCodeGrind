class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Given a 2D list of m x n dimensions, creates a list of elements in spiraling order
        Returns the answer as a list of ints
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        answer = []
        row = 0
        col = -1
        while rows and cols:
            for count in range(cols):
                col += 1
                answer.append(matrix[row][col])
            cols -= 1
            for count in range(rows - 1):
                row += 1
                answer.append(matrix[row][col])
            rows -= 1
            if cols == 0 or rows == 0: break
            for count in range(cols):
                col -= 1
                answer.append(matrix[row][col])
            cols -= 1
            for count in range(rows - 1):
                row -= 1
                answer.append(matrix[row][col])
            rows -= 1
        return answer