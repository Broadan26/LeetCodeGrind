class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # m = height, n = width
        odds = 0
        rows = [0] * m
        cols = [0] * n
        for index in indices: # Determine if rows/cols are odd/even
            rows[index[0]] ^= 1
            cols[index[1]] ^= 1
        
        for row in range(m): # Count the number of odds
            for col in range(n):
                odds += rows[row] ^ cols[col]
        return odds