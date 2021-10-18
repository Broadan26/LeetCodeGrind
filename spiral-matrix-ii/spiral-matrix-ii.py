class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n < 1: # n too small
            return [[]]
        
        # Create matrix & track nums
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        prev = 1
        
        x, y, end_x, end_y = 0, 0, 1, 0
        for cell in range(n * n): # Iterate whole matrix
            matrix[y][x] = cell+1
            # Rotate
            if not 0 <= x + end_x < n or not 0 <= y + end_y < n or matrix[y+end_y][x+end_x] != 0:
                end_x, end_y = -end_y, end_x
            x, y = x + end_x, y + end_y
        return matrix
            