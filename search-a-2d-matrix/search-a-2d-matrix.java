class Solution 
{
    public boolean searchMatrix(int[][] matrix, int target) 
    {
        int width = matrix[0].length;
        int height = matrix.length;

        int low = 0, hi = (width * height) - 1;
        while (low <= hi)
        {
            int mid = (low + hi) / 2;
            int row = mid / width;
            int col = mid % width;
            
            if (matrix[row][col] == target)
                return true;
            else if (matrix[row][col] < target)
                low = mid+1;
            else
                hi = mid-1;
        }
        return false;
    }
}