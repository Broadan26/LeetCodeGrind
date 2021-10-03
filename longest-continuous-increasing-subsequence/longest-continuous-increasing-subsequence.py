class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        current = 1
        for num in range(1, len(nums)):
            if nums[num] > nums[num-1]:
                current += 1
            else:
                longest = max(current, longest)
                current = 1
        return max(longest, current)