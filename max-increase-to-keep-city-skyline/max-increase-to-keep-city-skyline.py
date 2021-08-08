class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        '''
        Determines the total sum of building height increase without altering the skyline
        Returns the sum as an int
        '''
        sum = 0
        rows = [0] * len(grid)
        cols = [0] * len(grid)
        for row in range(len(grid)): #Get max of rows
            rows[row] = max(grid[row])
        for col in range(len(grid)): #Get max of cols
            for row in range(len(grid)):
                if grid[row][col] > cols[col]:
                    cols[col] = grid[row][col]
        for row in range(len(grid)): #Determine if we should adjust building height
            for col in range(len(grid)):
                if grid[row][col] < min(rows[row], cols[col]):
                    sum += (min(rows[row], cols[col]) - grid[row][col])
        return sum