class Solution 
{
    public int[][] matrixReshape(int[][] mat, int new_r, int new_c) 
    {
        // Get original dimensions
        int original_r = mat.length;
        int original_c = mat[0].length;
        
        // If reshape not possible, return original
        if (original_r * original_c != new_r * new_c)
            return mat;
        
        // Create new 2D array
        int[][] newMatrix = new int[new_r][new_c];
        
        // Move values from old matrix to new matrix
        int count = 0;
        for(int o_r = 0; o_r < original_r; o_r++)
            for(int o_c = 0; o_c < original_c; o_c++)
            {
                newMatrix[count / new_c][count % new_c] = mat[o_r][o_c];
                count++;
            }
        
        return newMatrix;
    }
}