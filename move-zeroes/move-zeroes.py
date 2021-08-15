class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        Given a list nums of ints, moves all the zeroes to the end
        Performs the move in-place
        '''
        count = 0
        for i in range(len(nums)):
            if nums[i - count] == 0:
                nums.pop(i - count)
                count += 1
        while count > 0:
            nums.append(0)
            count -= 1
        return None