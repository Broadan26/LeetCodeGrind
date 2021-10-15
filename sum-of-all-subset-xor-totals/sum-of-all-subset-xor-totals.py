class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for num in nums:
            bits |= num
        return bits * int(pow(2, len(nums)-1))