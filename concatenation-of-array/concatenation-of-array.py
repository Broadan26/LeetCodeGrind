class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        Given a list of ints nums, creates a duplicate list that is appended to the end of the original
        Returns the list of integers
        '''
        length = len(nums)
        for i in range(length):
            nums.append(nums[i])
        return nums