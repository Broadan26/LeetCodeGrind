class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        '''
        Determines the most amount of stones the first person pulling can get
        Returns the most stones as an int
        '''
        length = len(piles)
        mem = [[None]*(2*length) for _ in range(length)]

        def Helper(i, M):
            if i >= length: #Cannot perform
                return 0
            if mem[i][M] is not None: #Return remaining
                return mem[i][M]
            result = float('-inf') #Set result impossibly low
            sums = 0
            for k in range(1, 2*M + 1): #Determine the sum of a pile
                if i + k <= length:
                    sums += piles[i + k - 1]
                    result = max(result, sums - Helper(i + k, max(M, k))) #Determine the max and recurse
                else:
                    break
            mem[i][M] = result #Set result in table
            return result

        return (Helper(0, 1) + sum(piles)) // 2