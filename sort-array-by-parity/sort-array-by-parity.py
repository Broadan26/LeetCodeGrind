class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            if nums[lo] % 2 > nums[hi] % 2:
                nums[lo], nums[hi] = nums[hi], nums[lo]
            if nums[lo] % 2 == 0:
                lo += 1
            if nums[hi] % 2 == 1:
                hi -= 1
        return nums