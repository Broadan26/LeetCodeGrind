class Solution:
    #Function always returns true due to game setup
    #First person can always take the most optimal route
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        Determines if the first person taking stones wins the game
        Assumes both play optimally
        Returns true if the first person wins
        '''
        return True