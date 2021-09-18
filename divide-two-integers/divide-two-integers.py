class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #Setup boundaries of the problem
        MIN_VAL = -2147483648
        MAX_VAL = 2147483647

        #If divisor is trivial
        if abs(divisor) == 1:
            if dividend == MIN_VAL and divisor == -1:
                return MAX_VAL
            else:
                return dividend if divisor > 0 else -1 * dividend
        
        #Setup the problem to solve
        sign = -1 if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0) else 1
        answer = 0
        shift = 31
        dividend = abs(dividend)
        divisor = abs(divisor)

        #Perform division using bit shifts
        while dividend >= divisor:
            while dividend < (divisor << shift):
                shift -= 1
            dividend = dividend - (divisor << shift)
            answer = answer + (1 << shift)
        
        #Check if answer in boundaries
        answer = min(MAX_VAL, max(MIN_VAL, answer))

        return answer if sign > 0 else -1 * answer