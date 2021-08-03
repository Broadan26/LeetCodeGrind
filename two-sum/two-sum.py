class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given an array of integers and a target
        Returns the indices of two numbers in the array that add up to the target
        '''
        required = {} #Check for remaining value
        for i in range(len(nums)): #Check n-1 values
            if target - nums[i] in required: #If needed value is in array, return
                return [required[target - nums[i]], i]
            else: #Else add to checked array for later comparison at spot
                required[nums[i]] = i