class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        Sorts a list of numbers that represent colors so that they are adjacent to like colors
        0 = Red, 1 = White, 2 = Blue
        Performs the sort in-place on the list
        '''
        for idx in range(1, len(nums)): #Insertion SOrt, first element is sorted
            passes = 0
            while nums[idx-passes-1] > nums[idx-passes] and passes < idx: #Swap until in-place
                temp = nums[idx-passes-1]
                nums[idx-passes-1] = nums[idx-passes]
                nums[idx-passes] = temp
                passes += 1