class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        '''
        Given a list of integers, rearranges them as a permutation with the integer value in nums serving as the new index
        Returns the rearranged list of integers
        '''
        new_list = []
        for i in range(len(nums)):
            new_list.append(nums[nums[i]])
        return new_list