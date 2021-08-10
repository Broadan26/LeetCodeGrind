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
            if nums[mid] > nums[mid + 1]: #Values stopped increasing, found lowest
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]: #Found an increase to left, mid must be lowest
                return nums[mid]

            if nums[mid] > nums[0]: #Still iterating highest values
                left = mid + 1
            else:
                right = mid - 1