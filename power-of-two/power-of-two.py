class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        Given an integer n, determines if the value of n is a power of 2
        Returns True if it is, False otherwise
        '''
        if n is 1: #Power of 2^k is 0
            return True

        k = 1
        while k < n:
            k *= 2
            if k == n:
                return True
        return False