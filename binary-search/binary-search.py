class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums)-1
        lo = 0
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return -1