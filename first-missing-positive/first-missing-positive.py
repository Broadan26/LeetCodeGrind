class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n): # Remove negatives/greater than n's from consideration
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
        
        for i in range(n): # Record we have seen this element
            if 1 <= nums[i] % (n+1) <= n:
                ind = nums[i] % (n+1) - 1
                nums[ind] += n + 1
        for i in range(n): # Find the first value we never saw
            if nums[i] <= n:
                return i + 1
        return n+1