class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        hold = float('-inf')
        rest = 0
        for price in range(len(prices)):
            hold = max(hold, rest-prices[price])
            rest = max(rest, sold)
            sold = hold + prices[price]
        return max(sold, rest)
        