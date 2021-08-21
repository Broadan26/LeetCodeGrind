class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        Searches for a target value in a sorted list that has been rotated
        Returns true if the target is found, false otherwise
        '''
        numsSet = set(nums) #Convert list to a set
        return target in numsSet #Check if value in set