class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_of_coins = [float('inf') for _ in range(amount+1)]
        num_of_coins[0] = 0
        for coin in coins:
            for i in range(amount+1):
                if coin <= i:
                    num_of_coins[i] = min(num_of_coins[i], 1+num_of_coins[i-coin])
        return num_of_coins[amount] if num_of_coins[amount] != float('inf') else -1