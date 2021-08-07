class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Finds the element that appears at least floor(n/2) times in array
        Returns the int value of that element
        '''
        count = 0
        candidate = float('-inf')
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate