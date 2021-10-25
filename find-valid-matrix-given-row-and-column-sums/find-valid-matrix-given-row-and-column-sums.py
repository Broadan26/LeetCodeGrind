class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        if not rowSum or not colSum: # Cannot create matrix
            return []
        
        # Create the matrix
        answer = [[0] * len(colSum) for i in range(len(rowSum))]
        
        # Run through each element & pick min to place
        # Guarantees at least 1 valid matrix
        for row in range(len(rowSum)):
            for col in range(len(colSum)):
                answer[row][col] = min(rowSum[row], colSum[col])
                rowSum[row] -= answer[row][col]
                colSum[col] -= answer[row][col]
        return answer