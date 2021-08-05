class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Determines the max profit to be made buying a stock 1 day and selling on another day
        Returns the max profit
        '''
        min_price = float('inf')
        most_profit = 0
        for i in range(len(prices)): #Search for lowest valley and highest price afterwards
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > most_profit:
                most_profit = prices[i] - min_price
        return most_profit