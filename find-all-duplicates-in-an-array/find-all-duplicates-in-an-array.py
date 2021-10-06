class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                answer.append(abs(num))
            else:
                nums[(abs(num)-1)] *= -1
        return answer