class Solution 
{
    public int numRookCaptures(char[][] board) 
    {
        // Find the rook
        int rookRow = 0, rookCol = 0;
        for (int row = 0; row < board.length; row++)
            for (int col = 0; col < board[0].length; col++)
                if (board[row][col] == 'R')
                {
                    rookRow = row;
                    rookCol = col;
                    break;
                }
        
        // Setup attacks and hashset of friendly pieces
        int attacks = 0;
        Set<Character> friendly = new HashSet<Character>(Arrays.asList('B', 'R'));
        
        // Find North attacks
        for (int row = rookRow-1; row > -1; row--)
        {
            if (friendly.contains(board[row][rookCol]))
                break;
            else if (board[row][rookCol] != '.')
            {
                attacks++;
                break;
            }
        }
        // Find South attacks
        for (int row = rookRow+1; row < board.length; row++)
        {
            if (friendly.contains(board[row][rookCol]))
                break;
            else if (board[row][rookCol] != '.')
            {
                attacks++;
                break;
            }
        }
        // Find East attacks
        for (int col = rookCol+1; col < board[0].length; col++)
        {
            if (friendly.contains(board[rookRow][col]))
                break;
            else if (board[rookRow][col] != '.')
            {
                attacks++;
                break;
            }
        }
        // Find West attacks
        for (int col = rookCol-1; col > -1; col--)
        {
            if (friendly.contains(board[rookRow][col]))
                break;
            else if (board[rookRow][col] != '.')
            {
                attacks++;
                break;
            }
        }
        return attacks;
    }
}