class Solution 
{
    public boolean searchMatrix(int[][] matrix, int target) 
    {
        // No matrix to search
        if (matrix == null || matrix.length < 1 || matrix[0].length < 1) return false;
        
        // Search for target starting in top right corner
        int row = 0, col = matrix[0].length-1;
        while (col > -1 && row < matrix.length)
        {
            if (target == matrix[row][col]) return true;
            else if (target < matrix[row][col]) col--;
            else if (target > matrix[row][col]) row++;
        }
        return false;
    }
    
    /* Same idea as above, just starting in bottom left corner*/
//     public boolean searchMatrix(int[][] matrix, int target)
//     {
//         if (matrix == null || matrix.length < 1 || matrix[0].length < 1) return false;
        
//         int row = matrix.length-1, col = 0;
//         while (col < matrix[0].length && row > -1)
//         {
//             if (target == matrix[row][col]) return true;
//             else if (target < matrix[row][col]) row--;
//             else col++;
//         }
//         return false;
//     }
}