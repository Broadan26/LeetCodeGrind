class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        Solving the problem as intended using iteration
        Slower than average for this reason
        '''
        solution = 1.0
        power = n
        if n < 0:
            power *= -1
        while power:
            if power % 2:
                solution *= x
                power -= 1
            else:
                x *= x
                power /= 2
        if n < 0:
            solution = 1.0 / solution
        return solution
