class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        s_dict = Counter(s)
        count = 0
        for ch in t:
            if s_dict[ch] > 0:
                s_dict[ch] -= 1
            else:
                count += 1
        return count