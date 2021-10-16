class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)-1
        return (nums[length] - 1) * (nums[length-1] -1)