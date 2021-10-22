class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set(candyType) # Create a set of all candy types
        return min(len(candy_set), len(candyType)//2)