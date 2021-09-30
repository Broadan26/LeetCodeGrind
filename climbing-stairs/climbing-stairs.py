class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: #For n < 4 it's n
            return n
        #Otherwise Fibonacci, Powers take logn time
        return int((1 / math.sqrt(5)) * (((1 + math.sqrt(5))/ 2)**(n + 1) - ((1 - math.sqrt(5))/2)**(n + 1)))