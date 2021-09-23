class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        row = 0
        col = 0

        def dfs(grid, row, col, islands):
            if row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col] == '0':
                return
            if grid[row][col] == '1':
                grid[row][col] = '0'
                if row < len(grid)-1:
                    dfs(grid, row+1, col, islands)
                if col < len(grid[0]):
                    dfs(grid, row, col+1, islands)
                if col != 0:
                    dfs(grid, row, col-1, islands)
                if row != 0:
                    dfs(grid, row-1, col, islands)
            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(grid, row, col, islands)
        return islands