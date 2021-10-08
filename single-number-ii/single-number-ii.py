class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        negative = False
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1
            if count % 3 == 1:
                answer += (2 ** i)
                if i == 31:
                    negative = True
        return answer if not negative else answer - (2**32)