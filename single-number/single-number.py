class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Determines the number that exists in the list only one time
        Returns that number
        '''
        answer = 0
        for i in nums: #XOR every item in the list
            answer ^= i
        return answer