class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        if len(s) < 1:
            return 0
        
        s_dict = Counter(s)
        odd_longest, p_longest = 0, 0
        for key, val in s_dict.items():
            if val % 2 == 0: # Even number of vals
                p_longest += val
                
            elif val > odd_longest: # New largest odd num of vals
                p_longest += val
                if odd_longest > 0:
                    p_longest -= 1
                odd_longest = val
                
            else: # Get even num from odd num of vals
                p_longest += val - 1
                
        return p_longest