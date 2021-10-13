class Solution:
    def findComplement(self, num: int) -> int:
        answer = 1
        while answer <= num:
            answer = answer << 1
        return (answer - 1) ^ num