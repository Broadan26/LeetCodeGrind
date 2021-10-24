class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)-1, -1, -1):
            for col in range(len(grid[row])-1, -1, -1):
                if grid[row][col] < 0:
                    count += 1
                else:
                    break
        return count