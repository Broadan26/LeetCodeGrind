class Solution 
{
    public int maxAreaOfIsland(int[][] grid) 
    {
        if (grid.length < 1 || grid[0].length < 1) // Impossible
            return 0;
        
        int maxArea = 0;
        for (int row = 0; row < grid.length; row++)
        {
            for (int col = 0; col < grid[0].length; col++)
            {
                if (grid[row][col] == 1)
                    maxArea = Math.max(DFS(grid, row, col), maxArea);
            }
        }
        return maxArea;
    }
    
    public int DFS(int[][] grid, int row, int col)
    {
        if (row < 0 || row > grid.length-1) // Out of bounds
            return 0;
        if (col < 0 || col > grid[0].length-1) // Out of bounds
            return 0;
        if (grid[row][col] == 0)
            return 0;
        int area = 1;
        grid[row][col] = 0;
        area += DFS(grid, row+1, col);
        area += DFS(grid, row-1, col);
        area += DFS(grid, row, col+1);
        area += DFS(grid, row, col-1);
        return area;
    }
}