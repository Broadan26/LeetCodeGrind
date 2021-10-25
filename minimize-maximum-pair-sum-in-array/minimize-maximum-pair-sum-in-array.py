class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort() # Sort the list
        lo = 0
        hi = len(nums)-1
        nums_pair_max = float('-inf')
        while lo < hi:
            nums_pair_max = max(nums[lo]+nums[hi], nums_pair_max)
            lo += 1
            hi -= 1
        return nums_pair_max