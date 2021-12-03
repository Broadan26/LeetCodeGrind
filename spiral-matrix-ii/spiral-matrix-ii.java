class Solution 
{
    public int[][] generateMatrix(int n) 
    {
        // Create the 2D array
        int[][] answer = new int[n][n];
        
        // Run through the 2D array to fill in with updating count
        int row = 0, col = 0, count = 1;
        while (count <= n * n)
        {
            // Left -> Right
            while (col != n && answer[row][col] == 0)
            {
                answer[row][col] = count;
                col += 1;
                count += 1;
            }
            col -= 1; row += 1;
            
            // Top -> Bottom
            while (row != n && answer[row][col] == 0)
            {
                answer[row][col] = count;
                row += 1;
                count += 1;
            }
            row -= 1; col -= 1;
            
            // Right -> Left
            while (col > -1 && answer[row][col] == 0)
            {
                answer[row][col] = count;
                col -= 1;
                count += 1;
            }
            col += 1; row -= 1;
            
            // Bottom -> Top
            while (row > -1 && answer[row][col] == 0)
            {
                answer[row][col] = count;
                row -= 1;
                count += 1;
            }
            row += 1; col += 1;
        }
        
        return answer;
    }
}