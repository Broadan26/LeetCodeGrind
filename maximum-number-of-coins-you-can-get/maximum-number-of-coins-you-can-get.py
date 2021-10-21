class Solution:
    # def maxCoins(self, piles: list[int]) -> int:
    #     '''Straightforward brute force'''
    #     piles.sort() # Sort to find coins
    #     coin_max = 0
    #     while piles:
    #         second = piles[len(piles)-2] # You draw
    #         coin_max += second # Increment max
    #         piles = piles[1:-2] # Remove used elements
    #     return coin_max
    
    def maxCoins(self, piles: list[int]) -> int:
        '''More clean approach'''
        piles.sort()
        coin_max = 0
        for idx in range(len(piles)-1, len(piles)//3, -2):
            coin_max += piles[idx-1]
        return coin_max