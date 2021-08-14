class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        Given a value for n, determines how many trailing zeroes are in factorial(n)
        Returns the number of trailing zeroes
        '''
        count = 0
        while n > 0:
            count += n // 5
            n //= 5
        return count