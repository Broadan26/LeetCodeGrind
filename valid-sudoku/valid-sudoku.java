class Solution 
{
    public boolean isValidSudoku(char[][] board) 
    {
        return rowValids(board) && colValids(board) && squareValids(board);
    }
    
    /* Ensure rows are valid */
    public boolean rowValids(char[][] board)
    {
        for(int row = 0; row < board.length; row++)
        {
            HashSet<Character> rows = new HashSet<Character>();
            for(int col = 0; col < 9; col++)
            {
                if (board[row][col] != '.' && !rows.add(board[row][col]))
                    return false;
            }
        }
        return true;
    }
    
    public boolean colValids(char[][] board)
    {
        for(int row = 0; row < board.length; row++)
        {
            HashSet<Character> cols = new HashSet<Character>();
            for(int col = 0; col < 9; col++)
            {
                if (board[col][row] != '.' && !cols.add(board[col][row]))
                    return false;
            }
        }
        return true;
    }
    
    public boolean squareValids(char[][] board)
    {
        for(int row = 0; row < board.length; row++)
        {
            HashSet<Character> squares = new HashSet<Character>();
            for(int col = 0; col < board.length; col++)
            {
                int rowIdx = 3 * (row/3);
                int colIdx = 3 * (row%3);
                if (board[rowIdx + col/3][colIdx + col%3] != '.' && !squares.add(board[rowIdx + col/3][colIdx + col%3]))
                    return false;
            }
        }
        
        return true;
    }
}