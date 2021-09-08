class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Given a sorted list which is rotated around a pivot, find if the target value is in the list
        If the target is in the list, returns the index, otherwise returns -1
        '''
        lo = 0
        hi = len(nums) - 1
        pivot = nums[0]
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[lo] == target:
                return lo
            elif nums[hi] == target:
                return hi
            elif nums[mid] == target:
                return mid
            if target < pivot:
                lo += 1
            else:
                hi -= 1
        return -1