class Solution:
    # BRUTE FORCE: TOO SLOW
    # def numTeams(self, rating: list[int]) -> int:
    #     count = 0
    #     for i in range(0, len(rating)-2):
    #         for j in range(i+1, len(rating)-1):
    #             for k in range(j+1, len(rating)):
    #                 if rating[i] < rating[j] < rating[k]:
    #                     count += 1
    #                 elif rating[i] > rating[j] > rating[k]:
    #                     count += 1
    #     return count
    
    def numTeams(self, rating: list[int]) -> int:
        asc = dsc = 0
        for idx, val in enumerate(rating):
            llc = rgc = lgc = rlc = 0
            for l in rating[:idx]: # Count left of index
                if l < val:
                    llc += 1
                if l > val:
                    lgc += 1
            for r in rating[idx+1:]: # Count right of index
                if r > val:
                    rgc += 1
                if r < val:
                    rlc += 1
            asc += llc * rgc # Multiply to get sequences
            dsc += lgc * rlc
        return asc + dsc