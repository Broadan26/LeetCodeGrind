class Solution:
    def minOperations(self, nums: List[int]) -> int:
        changes = 0
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx-1]: # Check if prev num bigger than current
                temp = (nums[idx-1] - nums[idx]) + 1 # Increment by 1 more
                nums[idx] += temp # Increment
                changes += temp # Save changes
        return changes