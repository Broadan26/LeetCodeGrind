class Solution:
    def addDigits(self, num: int) -> int:
        '''
        Takes an integer and continuously adds all its digits until only a single digit is left
        Repeats the process until the sum of the digits is a single digit
        Returns that final value as an int
        '''
        while num > 9: #Run while the number is 2 or more digits
            value = 0
            while num != 0: #Find the sum of the current number's digits
                value += (num % 10)
                num = num // 10
            num = value
        return num