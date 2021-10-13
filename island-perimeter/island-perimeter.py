class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        islands = neighbors = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1: # Found an island
                    islands += 1
                    if row < len(grid)-1 and grid[row+1][col] == 1: # Check down
                        neighbors += 1
                    if col < len(grid[row])-1 and grid[row][col+1] == 1: # Check right
                        neighbors += 1
        return (islands * 4) - (neighbors * 2) # 4 sides, 2 potential neighbors