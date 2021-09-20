class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        #Setup the winning conditions
        n = 3
        rows = [0] * n
        cols = [0] * n
        diag = 0
        anti_diag = 0

        #Setup who starts first
        player = 1

        #Play each move
        for row, col in moves:
            rows[row] += player
            cols[col] += player
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player

            #Check if someone has won
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return 'A' if player == 1 else 'B'
            player *= -1 # Change turns

        return 'Draw' if len(moves) == n * n else 'Pending' #Draw of incomplete conditions