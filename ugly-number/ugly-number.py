class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        Given an int n, determines if n is divisible by only prime factors 2,3,5
        Returns True if it is, false otherwise
        '''
        if n < 1:
            return False
        while n > 1:
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
        return n == 1