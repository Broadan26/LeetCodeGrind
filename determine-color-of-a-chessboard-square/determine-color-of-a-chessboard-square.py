class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha_map = [1,2,3,4,5,6,7,8] # Translate board to 2D list
        row = int(coordinates[1])
        col = alpha_map[ord(coordinates[0])-97]
        
        if row % 2 == 0 and col % 2 == 0:
            return False
        elif row % 2 == 0 and col % 2 != 0:
            return True
        elif row % 2 != 0 and col % 2 == 0:
            return True
        else:
            return False