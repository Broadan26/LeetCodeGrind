class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        '''
        Given a list of numbers that are a permutation of the length of the list
        Finds the longest cycle using the index and assigned value as pointers
        Returns the longest cycle as an int
        '''
        answer = 0
        for num in nums: #Iterate each cycle in the list
            if num == -1: continue
            count = 0
            while nums[num] != -1: #If not visited, keep visiting
                count += 1
                nums[num], num = -1, nums[num]
            answer = max(answer, count) #Store the longest cycle
        return answer