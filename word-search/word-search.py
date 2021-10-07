class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        self.word = word
        self.found = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.visited = []
                self.visitedSet = set()
                self.dfs(board, row, col, 0)
                if self.found:
                    return True
        return False
    
    def dfs(self, board: list[list[int]], row: int, col: int, count: int):
        if count == len(self.word):
            self.found = True
        if not self.found and row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and board[row][col] == self.word[count] and (row, col) not in self.visitedSet:
            self.visited += [(row,col)]
            self.visitedSet.add((row,col))
            self.dfs(board,row+1,col,count+1)
            self.dfs(board,row-1,col,count+1)
            self.dfs(board,row,col+1,count+1)
            self.dfs(board,row,col-1,count+1)
            
            if not self.found:
                self.visitedSet.remove(self.visited.pop())