class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0 # Add 1 for each non-zero element in the grid
        side = 0 # Takes the largest value in the column
        front = 0 # Takes the largest value in each row
        for row in range(len(grid)):
            side_max = 0
            front_max = 0
            for col in range(len(grid[row])):
                if grid[row][col]: top += 1
                side_max = max(side_max, grid[row][col])
                front_max = max(front_max, grid[col][row])
            side += side_max
            front += front_max
        return top + side + front