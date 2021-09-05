class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        Given two integers a and b, returns the sum without using built-in operators
        Returns the sum of a and b as an int
        '''
        mask = 0xffffffff #Avoid overflow with negatives
        while (b & mask > 0): #While b is not 0 and mask is not 0
            carry = a & b # And the two numbers for carry
            a = a ^ b # XOR to perform addition
            b = carry << 1 # Remove the last bit from carry
        return (a & mask) if b > 0 else a