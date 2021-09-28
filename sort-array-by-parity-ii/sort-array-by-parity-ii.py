class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenP = 0
        oddP = len(nums) - 1
        while evenP < len(nums) and oddP >= 0:
            while evenP < len(nums) and nums[evenP] % 2 == 0: # Run until odd in even spot
                evenP += 2
            while oddP > 0 and nums[oddP] % 2 != 0: # Run until even in odd spot
                oddP -= 2

            if evenP > len(nums) or oddP < 0: break # Went too far past list bounds

            nums[evenP], nums[oddP] = nums[oddP], nums[evenP]
        return nums