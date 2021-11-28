class Solution 
{
    public void gameOfLife(int[][] board) 
    {
        // Nothing can be done
        if (board.length < 1 || board[0].length < 1) return;
        
        // Determine the next state
        boolean[][] next = new boolean[board.length][board[0].length];
        
        // Setup a list of directions the algorithm will follow
        int[][] directions = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
        
        // Compare current board with next board conditions
        for (int row = 0; row < board.length; row++)
        {
            for (int col = 0; col < board[row].length; col++)
            {
                int count = 0;
                for (int[] direction : directions) // Check directions
                    if (row + direction[0] > -1 && row + direction[0] < board.length 
                        && col + direction[1] > -1 && col + direction[1] < board[row].length 
                        && board[row+direction[0]][col+direction[1]] == 1)
                    {
                        count += 1;
                    }
                
                // Update status
                if (board[row][col] == 1 && count > 1 && count < 4) next[row][col] = true;
                else if (count == 3) next[row][col] = true;
            }
        }
        
        // Update the next board state in-place
        for (int row = 0; row < board.length; row++)
            for (int col = 0; col < board[row].length; col++)
                board[row][col] = next[row][col] ? 1 : 0;
    }
}