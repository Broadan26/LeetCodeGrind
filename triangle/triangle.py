class Solution:
    # [0] finish
    # [0, 1] ^
    # [0, 1, 2] ^
    # [0, 1, 2, 3] ^ start
    # [0, 1, 2, 3, 4]
    
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for row in range(len(triangle)-2, -1, -1): # Start from bottom
            for col in range(len(triangle[row])-1, -1, -1): # Work backwards thru rows
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1]) # Dynamically allocate data
        return triangle[0][0]