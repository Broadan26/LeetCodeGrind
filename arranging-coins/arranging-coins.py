class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + .25)**.5 -.5)