class Solution 
{
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) 
    {
        if (image.length == 0) // No image given
            return image;
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length) // Point out of bounds
            return image;
        
        int origColor = image[sr][sc];
        if (origColor != newColor) 
            dfs(image, sr, sc, origColor, newColor);
        return image;
    }
    
    public void dfs(int[][] image, int row, int col, int origColor, int newColor)
    {
        if (image[row][col] == origColor)
        {
            image[row][col] = newColor;
            if (row >= 1) dfs(image, row-1, col, origColor, newColor);
            if (col >= 1) dfs(image, row, col-1, origColor, newColor);
            if (row+1 < image.length) dfs(image, row+1, col, origColor, newColor);
            if (col+1 < image[0].length) dfs(image, row, col+1, origColor, newColor);
        }
    }
}