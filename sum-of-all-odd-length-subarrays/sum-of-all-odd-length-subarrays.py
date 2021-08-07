class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        '''
        Returns the sum of all odd-length subarrays in the given array
        Returns the value as an int
        '''
        result = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                result += sum(arr[i:j+1])
        return result