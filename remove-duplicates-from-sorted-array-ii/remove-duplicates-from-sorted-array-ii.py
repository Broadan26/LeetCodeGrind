class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        index = 0
        while index < length: # Run the length of the array
            count = 0
            curr_num = nums[index]
            while index < length and nums[index] == curr_num: # Check elements
                if count < 2: # Iterate elements
                    count += 1
                    index += 1
                else: # Remove incorrect elements
                    nums.pop(index)
                    length -= 1
        return length