class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Determines if the number n is a happy number
        Returns true if it is, false otherwise
        '''
        seen = set() #Hash table O(1) comparison, O(n) space
        while n > 1 and n not in seen: #Happy conditions
            seen.add(n)
            n = self.sumHelper(n)
        return (n == 1)
    
    def sumHelper(self, n: int) -> int:
        '''
        Generates the sum of the power of n's digits
        Returns the new number
        '''
        sum = 0
        while n > 0: #
            temp = n % 10
            sum += temp ** 2
            n = n // 10
        return sum