class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed_nums = set()
        length = 0
        while length < len(nums):
            if nums[length] in removed_nums:
                nums.pop(length)
            else:
                removed_nums.add(nums[length])
                length += 1
        return length