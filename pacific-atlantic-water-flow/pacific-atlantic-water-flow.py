class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        answer = []
        dp = [0] * (len(heights) * len(heights[0]))

        def dfs(i: int, j: int, w: int, h: int):
            ij = i * len(heights[0]) + j
            if dp[ij] & w or heights[i][j] < h: return
            dp[ij] += w
            h = heights[i][j]
            if dp[ij] == 3: answer.append([i,j])
            if i + 1 < len(heights): dfs(i+1, j, w, h)
            if i > 0: dfs(i-1, j, w, h)
            if j + 1 < len(heights[0]): dfs(i, j+1, w, h)
            if j > 0: dfs(i, j-1, w, h)

        for row in range(len(heights)):
            dfs(row, 0, 1, heights[row][0])
            dfs(row, len(heights[0])-1, 2, heights[row][len(heights[0])-1])

        for col in range(len(heights[0])):
            dfs(0, col, 1, heights[0][col])
            dfs(len(heights)-1, col, 2, heights[len(heights)-1][col])

        return answer