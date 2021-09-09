class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) == 0: #nums is empty
            return ranges

        start = nums[0]
        prev = nums[0]
        for i in range(0, len(nums)):
            if start == prev and nums[i] > prev + 1: #Range is length 1
                ranges.append(str(start))
                start = nums[i]
            elif prev + 1 < nums[i]: #Range spans multiple digits
                ranges.append(str(start) + '->' + str(prev))
                start = nums[i]
            if prev + 1 == nums[i] and i + 1 == len(nums): #Range spans multiple digits, last iteration
                ranges.append(str(start) + '->' + str(nums[i]))
            prev = nums[i]
        if start == nums[len(nums)-1]: #In case last element wasn't handled
            ranges.append(str(start))
        return ranges