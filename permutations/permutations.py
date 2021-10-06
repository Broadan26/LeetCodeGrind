class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.dfs(nums, [], answer)
        return answer
    
    def dfs(self, nums: list[int], perm: list[int], answer: list[list[int]]):
        if not nums: # Finished iterating nums
            answer.append(perm)
        for i in range(len(nums)): #Cut off first kth num, append first kth num, keep transfering answer
            self.dfs(nums[:i] + nums[i+1:], perm+[nums[i]], answer)