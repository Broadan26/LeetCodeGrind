class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_set = set()
        seen_set = set()
        unique_sum = 0
        for num in nums:
            if num not in num_set:
                num_set.add(num)
                unique_sum += num
            elif num not in seen_set:
                unique_sum -= num
                seen_set.add(num)
        return unique_sum