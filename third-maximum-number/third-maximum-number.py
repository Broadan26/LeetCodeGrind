class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_set = sorted(list(set(nums)), reverse=True) # Remove duplicates and sort numbers
        if len(num_set) > 2:
            return num_set[2]
        else:
            return num_set[0]