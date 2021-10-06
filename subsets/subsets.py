class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''Returns the powerset of the list of nums'''
        answer = [[]] # Create empty set
        if not nums:
            return answer
        for num in nums:
            for i in range(len(answer)): # Append nums as they appear and build powerset over time
                answer.append(answer[i] + [num])
        return answer