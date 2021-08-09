class Solution:
    def multiplyEasy(num1: str, num2: str):
        '''
        Easiest possible solution to the problem
        But breaks all the rules
        '''
        return str(int(num1) * int(num2))
    
    def multiply(self, num1: str, num2: str) -> str:
        '''
        A more expanded solution to the problem without breaking rules
        Converts the numbers to integer by hand and converts them back to string
        '''
        sum1 = 0
        sum2 = 0
        for c in num1: #Convert num1 to int
            sum1 *= 10
            sum1 += ord(c) - 48
        for c in num2: #Convert num2 to int
            sum2 *= 10
            sum2 += ord(c) - 48
        return str(sum1 * sum2)
