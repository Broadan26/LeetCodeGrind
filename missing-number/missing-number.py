class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Given a list of nums from 0 to len(nums), finds the missing num in the list
        Returns the missing num as an int
        '''
        set_of_nums = set(nums)
        all_possible_nums = set(range(0, len(nums)+1))
        return all_possible_nums.difference(set_of_nums).pop()