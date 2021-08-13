class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Checks if a list has duplicates.
        If it does it returns True, otherwise False
        '''
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False