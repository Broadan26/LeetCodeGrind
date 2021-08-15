class Solution:
    def canWinNim(self, n: int) -> bool: 
        '''
        Determines if the player who goes first can win the game of nim
        Players takes 1-3 stones each time
        Returns true if player going first can win, otherwise false
        '''
        return (n % 4) != 0 #Player going first just needs to avoid a multiple of 4 to win
