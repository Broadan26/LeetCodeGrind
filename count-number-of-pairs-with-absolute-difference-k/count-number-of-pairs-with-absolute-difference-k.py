class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for idx in range(len(nums)-1):
            for j in range(idx+1, len(nums)):
                if abs(nums[idx] - nums[j]) == k:
                    count += 1
        return count