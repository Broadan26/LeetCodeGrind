class Solution:
    def minOperations(self, n: int) -> int:
        n -= 1
        if n % 2 != 0:
            return int(((n+1)**2) / 4)
        else:
            return int((((n+1)**2) - 1) / 4)