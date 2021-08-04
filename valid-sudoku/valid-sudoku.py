class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Determines if a Sudoku doesn't break any basic Sudoku rules
        Returns true if Sudoku is valid, otherwise false
        '''
        #Setup a bit mask to keep track of seen values
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9

        for r in range(0,9): #Iterate rows
            for c in range(0,9): #Iterate columns
                if board[r][c] != '.': #Only compare filled elements
                    current = int(board[r][c]) - 1

                    if rows[r] & (1 << current): #Compare if element present in row
                        return False
                    rows[r] |= (1 << current) #Push bit into list

                    if columns[c] & (1 << current): #Compare if element present in column
                        return False
                    columns[c] |= (1 << current)

                    b_loc = (r // 3) * 3 + c // 3 #Determine box location
                    if boxes[b_loc] & (1 << current): #Compare if element present in box
                        return False
                    boxes[b_loc] |= (1 << current)
        return True