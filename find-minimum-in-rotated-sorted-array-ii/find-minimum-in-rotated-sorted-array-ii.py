class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Takes a sorted array that has been rotated and finds the min value.
        Returns the minimum value
        '''
        length = len(nums)
        if nums[0] < nums[length - 1] or length == 1: #No rotations, size of 1
            return nums[0]
        left = 0
        right = length - 1
        while right >= left: #Find the max value which is the rotation start
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: 
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]