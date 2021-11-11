class Solution 
{
    public int[][] transpose(int[][] matrix) 
    {
        if (matrix.length < 1 && matrix[0].length < 1) // Not possible
            return matrix;
        
        int[][] newMatrix = new int[matrix[0].length][matrix.length];
        for (int row = 0; row < matrix.length; row++)
        {
            for (int col = 0; col < matrix[0].length; col++)
            {
                newMatrix[col][row] = matrix[row][col];
            }
        }
        return newMatrix;
    }
}