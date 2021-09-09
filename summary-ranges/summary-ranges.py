class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        while i < len(nums): #Handles the start of ranges
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1: #Checks for ranges extended multiple digits
                i += 1
            if start != nums[i]: #Ranges span multiple digits
                ranges.append(str(start) + '->' + str(nums[i]))
            else: #Ranges do not span multiple digits
                ranges.append(str(start))
            i += 1 #Continue
        return ranges
