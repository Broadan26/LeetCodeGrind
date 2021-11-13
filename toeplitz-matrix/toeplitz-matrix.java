class Solution 
{
    public boolean isToeplitzMatrix(int[][] matrix) 
    {
        if (matrix.length < 1 || matrix[0].length < 1) // Not possible
            return false;
        
        // Compare cell in 2D array with cell up & to left
        for (int row = 0; row < matrix.length; row++)
            for (int col = 0; col < matrix[row].length; col++)
                if (row > 0 && col > 0 && matrix[row-1][col-1] != matrix[row][col])
                    return false;
        
        return true;
    }
}

// (0, 3)
// (0, 2) (1, 3)
// (0, 1) (1, 2) (2, 3)
// (0, 0) (1, 1) (2, 2)
// (1, 0) (2, 1)
// (2, 0)