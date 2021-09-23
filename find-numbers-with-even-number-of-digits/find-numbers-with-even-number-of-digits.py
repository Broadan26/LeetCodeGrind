class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            count = 0
            while num > 0:
                num //= 10
                count += 1
            if count % 2 == 0:
                answer += 1

        return answer