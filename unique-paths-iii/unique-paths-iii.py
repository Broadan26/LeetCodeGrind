class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        start_x = start_y = 0
        empty_squares = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: # Count empty squares
                    empty_squares += 1
                elif grid[row][col] == 1: # Find the start
                    start_x, start_y = row, col
        return self.dfs(grid, start_x, start_y, -1, empty_squares)
        
    def dfs(self, grid: list[list[int]], start_x: int, start_y: int, count: int, empty_squares: int) -> int:
        if start_x < 0 or start_y < 0: # Out of bounds left/up
            return 0
        if start_x >= len(grid) or start_y >= len(grid[start_x]): # Out of bounds right/down
            return 0
        if grid[start_x][start_y] == -1: # On impassable terrain
            return 0
        
        # Check if end reached correctly
        if grid[start_x][start_y] == 2:
            if count == empty_squares:
                return 1
            else:
                return 0
        
        # Check possible paths
        grid[start_x][start_y] = -1
        total_paths = self.dfs(grid, start_x-1, start_y, count+1, empty_squares)
        total_paths += self.dfs(grid, start_x+1, start_y, count+1, empty_squares)
        total_paths += self.dfs(grid, start_x, start_y-1, count+1, empty_squares)
        total_paths += self.dfs(grid, start_x, start_y+1, count+1, empty_squares)
        
        grid[start_x][start_y] = 0 # Reset the grid
        
        return total_paths