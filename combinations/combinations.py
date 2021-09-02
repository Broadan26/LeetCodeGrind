class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(start, path):
            if len(path) + 1 == k: #Add the final element of possible paths
                for i in range(start+1, n+1):
                    answer.append(path + [i])
            else:
                for i in range(start+1, n+1): #Build the path
                    helper(i, path + [i])

        answer = []
        helper(0, [])
        return answer