class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        Given an integer for rows this generates Pascal's Triangle
        Returns a list of lists with Pascal's Triangle
        '''
        if numRows == 1: #Return 1 step
            return [[1]]
        elif numRows == 2: #Return 2 steps
            return [[1], [1,1]]
        triangle = [[1],[1,1]]
        for i in range(2, numRows): #Return n steps
            temp = []
            temp.append(1)
            for j in range(1, i): #Calculate intermediate pieces
                t1 = triangle[i-1][j-1]
                t2 = triangle[i-1][j]
                temp.append(t1 + t2)
            temp.append(1)
            triangle.append(temp)
        return triangle