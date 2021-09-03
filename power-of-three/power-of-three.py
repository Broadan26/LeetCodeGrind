class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        Given a number n, determine if it is a power of 3
        Returns True if it is, false otherwise
        '''
        if n < 0: #Negatives are not a power of three
            return False
        i = 1
        while i <= n: #Loop until at least n
            if i == n: #Check is equal
                return True
            i *= 3
        return False