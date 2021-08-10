class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Looks for elements in the list that are taller than both its neighbors.
        Returns the index of the element
        '''
        left = 0
        right = len(nums) - 1
        while left < right: #Iterate until two pointers cross
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: #Peak to the left
                right = mid
            else: #Peak to the right
                left = mid + 1
        return left
    
    def findPeakElementSlow(nums: list[int]) -> int: #Time Complexity O(n), Space Complexity O(1)
        for i in range(len(nums)):
            if nums[i] > nums[i + 1]: #Can actually handle plateaus
                return i
