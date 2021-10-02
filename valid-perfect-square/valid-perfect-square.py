class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for val in range(int(math.sqrt(num))+1):
            if (val * val) == num:
                return True
        return False