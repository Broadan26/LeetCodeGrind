class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Checks if there are duplicate values within k spaces of each other in a list
        If there are return True, otherwise return false
        '''
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            elif (i - dict[nums[i]]) <= k:
                return True
            else:
                dict[nums[i]] = i
        return False