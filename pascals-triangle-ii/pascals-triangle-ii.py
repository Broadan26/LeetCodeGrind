class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        Generates the row in Pascal's triangle to return
        Returns the requested row of Pascal's Triangle
        '''
        answer = [1]
        for i in range(1, rowIndex+1):
            spot = self.factorial(rowIndex) // (self.factorial(i) * self.factorial(rowIndex - i))
            answer.append(spot)
        return answer
    
    def factorial(self, n: int) -> int:
        val = 1
        for i in range(1, n+1):
            val *= i
        return val