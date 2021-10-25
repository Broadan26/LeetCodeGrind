class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for index in range(len(nums))[::-1]: # Work backwards
            if index + nums[index] >= last: # Check if we can reach current spot from earlier
                last = index
        
        #If at front of list, we can jump whole list
        return not last