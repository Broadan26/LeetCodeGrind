class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')
        current = 0
        for num in nums:
            current = max(num, current+num)
            largest = max(current, largest)
        return largest