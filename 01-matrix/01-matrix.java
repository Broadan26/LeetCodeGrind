class Solution 
{
    public int[][] updateMatrix(int[][] mat) 
    {
        // Setup the memoization
        int maxAway = mat.length + mat[0].length - 2;
        for (int row = 0; row < mat.length; row++)
            for (int col = 0; col < mat[row].length; col++)
            {
                if (mat[row][col] == 0) continue;
                else mat[row][col] = maxAway;
            }
        
        // Check top left to bottom right for 0's
        for (int row = 0; row < mat.length; row++)
            for (int col = 0; col < mat[row].length; col++)
            {
                if (mat[row][col] == 0) continue;
                if (row > 0) mat[row][col] = Math.min(mat[row-1][col] + 1, mat[row][col]);
                if (col > 0) mat[row][col] = Math.min(mat[row][col-1] + 1, mat[row][col]);
            }
        
        // Check bottom right to top left for 0's
        for (int row = mat.length-1; row >= 0; row--)
            for (int col = mat[row].length-1; col >= 0; col--)
            {
                if (mat[row][col] == 0) continue;
                if (row < mat.length-1)
                    mat[row][col] = Math.min(mat[row+1][col] + 1, mat[row][col]);
                if (col < mat[row].length-1)
                    mat[row][col] = Math.min(mat[row][col+1] + 1, mat[row][col]);
            }
        return mat;
    }
}