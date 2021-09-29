class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Given a list of nums from 0 to len(nums), finds the missing num in the list
        Returns the missing num as an int
        '''
        xor = 0
        for i in range(len(nums)):
            xor ^= (i+1)^nums[i]
        return xor