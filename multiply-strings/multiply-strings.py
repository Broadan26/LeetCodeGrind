class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum1 = 0
        sum2 = 0
        for c in num1: #Convert num1 to int
            sum1 *= 10
            sum1 += int(c)
        for c in num2: #Convert num2 to int
            sum2 *= 10
            sum2 += int(c)
        return str(sum1 * sum2)