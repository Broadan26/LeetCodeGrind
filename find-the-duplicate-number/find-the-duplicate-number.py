class Solution:
    
    def findDuplicate(self, nums: list[int]) -> int: # Breaks modifying list rule
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]
        return -1
            
    # def findDuplicate(self, nums: list[int]) -> int: # Breaks O(1) space rule
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return num
    #         seen.add(num)
    #     return -1
            
    
    # def findDuplicate(self, nums: list[int]) -> int: # Brute Force
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return nums[i]
    #     return -1