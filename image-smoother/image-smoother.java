class Solution 
{
    public int[][] imageSmoother(int[][] img) 
    {
        // Nothing can be done
        if (img.length < 1 || img[0].length < 1) return img;
        
        // Create a new smoothed image
        int[][] smoothed = new int[img.length][img[0].length];
        
        // Create a set of directions to check
        int[][] directions = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}, {0,0}};
        
        // Iterate each cell in the image
        for (int row = 0; row < img.length; row++)
        {
            for (int col = 0; col < img[0].length; col++)
            {
                // Smooth each cell
                int sum = 0, count = 0;
                for (int[] dir : directions)
                {
                    int currRow = row + dir[0];
                    int currCol = col + dir[1];
                    if (currRow > -1 && currRow < img.length && currCol > -1 && currCol < img[row].length)
                    {
                        sum += img[currRow][currCol];
                        count += 1;
                    }
                }
                smoothed[row][col] = sum / count;
            }
        }
        return smoothed;
    }
}