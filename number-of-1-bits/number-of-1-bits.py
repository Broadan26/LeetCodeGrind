class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Calculates the number of '1' bits in a bit string
        Returns the number of 1 bits
        '''
        count_ones = 0
        while n != 0:
            count_ones += 1
            n &= (n-1) # Keep popping 1's until n is 0
        return count_ones