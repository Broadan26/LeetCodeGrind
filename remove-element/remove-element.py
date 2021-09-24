class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        while length < len(nums):
            if nums[length] == val:
                nums.pop(length)
            else:
                length += 1
        return length