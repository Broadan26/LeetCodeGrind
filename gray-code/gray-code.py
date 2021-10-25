class Solution:
    def grayCode(self, n: int) -> list[int]:
        answer = [0]
        for i in range(1, 2**n):
            answer.append(answer[-1] ^ (i & -i))
        return answer