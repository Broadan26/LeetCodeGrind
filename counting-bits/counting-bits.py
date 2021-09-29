class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Generates the number 1's for each index value of the list
        Returns the list
        '''
        answer = [0]
        for i in range(1, n+1):
            answer.append(answer[i // 2] + (i % 2))
        return answer