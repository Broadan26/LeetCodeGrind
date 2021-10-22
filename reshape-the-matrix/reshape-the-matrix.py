class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (r * c) != (len(mat) * len(mat[0])):
            return mat
        answer = []
        curr_row = []
        count = 0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if (count % c) == 0 and curr_row:
                    answer.append(curr_row)
                    curr_row = []
                curr_row.append(mat[row][col])
                count += 1
        answer.append(curr_row)
        return answer
                    