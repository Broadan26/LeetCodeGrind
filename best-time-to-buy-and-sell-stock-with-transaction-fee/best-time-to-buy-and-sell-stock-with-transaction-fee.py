class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = float('-inf') # No stock held
        sold = 0 # No profit
        for price in range(0, len(prices)):
            old_sold = sold # Store last sale
            sold = max(sold, hold+prices[price]-fee) # Check if another sale good
            hold = max(hold, old_sold-prices[price]) # Check if another hold good
        return sold