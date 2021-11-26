class Solution 
{
    public int orangesRotting(int[][] grid) 
    {
        if (grid.length < 1 || grid[0].length < 1) // Not possible
            return -1;
        
        // Queue up rotten nodes and count fresh nodes
        Deque<int[]> queue = new LinkedList<int[]>();
        int fresh = 0;
        for (int row = 0; row < grid.length; row++)
        {
            for (int col = 0; col < grid[0].length; col++)
            {
                if (grid[row][col] == 2)
                    queue.offerLast(new int[]{row, col});
                else if (grid[row][col] == 1)
                    fresh++;
            }
        }
        if (fresh == 0) return 0; // No fresh nodes exist
        
        int count = 0;
        int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
        while (queue.size() > 0) // BFS
        {
            count += 1;
            int qSize = queue.size();
            // BFS from rotten nodes found initially
            for (int i = 0; i < qSize; i++)
            {
                int[] point = queue.pollFirst();
                for(int[] dir : directions)
                {
                    int x = point[0] + dir[0];
                    int y = point[1] + dir[1];
                    
                    // Out of bounds, cell is rotten, cell is empty
                    if (x < 0 || y < 0 || 
                        x >= grid.length || y >= grid[0].length || 
                        grid[x][y] == 0 || grid[x][y] == 2) continue;
                    
                    grid[x][y] = 2;
                    queue.offerLast(new int[]{x, y});
                    fresh -= 1;
                }
            }
        }
        return fresh == 0 ? count-1 : -1;
        }
}