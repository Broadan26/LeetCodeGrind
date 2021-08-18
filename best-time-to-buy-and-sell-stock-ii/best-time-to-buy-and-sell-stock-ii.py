class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Determines the max profit to be made buying a stock 1 day and selling on another day
        Multiple transactions can occur
        Returns the max profit
        '''
        maxProfit = 0
        for day in range(1, len(prices)): #Start from day 2 to check for increase/decrease
            if prices[day] > prices[day - 1]: #If price increases, add the difference to profit
                maxProfit += prices[day] - prices[day - 1]
        return maxProfit