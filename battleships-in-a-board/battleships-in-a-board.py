class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        '''
        Counts the number of 'battleships' present on a 2D array
        A battleship being a continuous set of X's in a singular direction
        Returns the number of battleships as an int
        '''
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'X': #Start checking for battleship when X found
                    if row == 0 and col == 0: #Edges case handler
                        count += 1
                    elif row == 0: #Edge case when on top of 2D array
                        if board[row][col-1] != 'X':
                            count += 1
                    elif col == 0: #Edge case when in first col of 2D array
                        if board[row - 1][col] != 'X':
                            count += 1
                    elif board[row - 1][col] == '.' and board[row][col - 1] == '.': #Count battleships when X's lined up
                        count += 1
        return count