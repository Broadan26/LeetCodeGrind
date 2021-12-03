class Solution 
{
    public void rotate(int[][] matrix) 
    {
        // Nothing to do
        if (matrix.length < 1 || matrix[0].length < 1)
            return;
        
        // Calculate the number of sections to rotate
        int length = matrix.length;
        for (int i = 0; i < (length / 2) + length % 2; i++)
        {
            // Calculate the number of cells that need to be rotated per section
            for (int j = 0; j < length / 2; j++)
            {
                // Rotate 4 points at once
                int temp = matrix[length-1-j][i];
                matrix[length-1-j][i] = matrix[length-1-i][length-j-1];
                matrix[length-1-i][length-j-1] = matrix[j][length-1-i];
                matrix[j][length-1-i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
    }
}