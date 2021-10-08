class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        the_sum = 0 # Sum of two single nums
        for num in nums:
            the_sum ^= num
        diff = 1 # Find out the difference between the two numbers
        while (diff & the_sum) == 0:
            diff = diff << 1
        num1 = num2 = 0
        for num in nums: # Go thru array to locate where diff occurs
            if num & diff == 0: # Found second single num
                num1 ^= num
            else: # Single Num solution
                num2 ^= num
        return [num1, num2]