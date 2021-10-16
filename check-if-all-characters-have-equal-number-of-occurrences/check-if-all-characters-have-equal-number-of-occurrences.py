class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        s_dict = Counter(s)
        match = s_dict[s[0]]
        for val in s_dict.values():
            if val == match:
                continue
            else:
                return False
        return True