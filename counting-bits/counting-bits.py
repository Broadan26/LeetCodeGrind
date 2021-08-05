class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Generates the number 1's for each index value of the list
        Returns the list
        '''
        result = [0]
        for i in range(1, n+1):
            temp = result[i // 2] + i % 2
            result.append(temp)
        return result