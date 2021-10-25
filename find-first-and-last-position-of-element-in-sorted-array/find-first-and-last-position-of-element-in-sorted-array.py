class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1,-1]