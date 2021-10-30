class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        nums_dict = Counter(nums)
        missing = extra = 0
        for i in range(1, len(nums)+1):
            if nums_dict[i] > 1:
                extra = i
            elif i not in nums_dict:
                missing = i
        return [extra, missing]