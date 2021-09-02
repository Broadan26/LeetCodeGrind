class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Given two strings, determines if the strings are anagrams
        If they are, returns true, otherwise false
        '''
        from collections import Counter
        dic_S = Counter(s)
        dic_T = Counter(t)
        return dic_S == dic_T