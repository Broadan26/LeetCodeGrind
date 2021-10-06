class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        nums.sort()
        set_of_answer = set()
        if not nums: # Nums only contains empty set
            return answer
        for num in nums:
            for i in range(len(answer)):
                if tuple(answer[i] + [num]) not in set_of_answer:
                    answer.append(answer[i] + [num])
                    set_of_answer.add(tuple(answer[-1]))
        return answer