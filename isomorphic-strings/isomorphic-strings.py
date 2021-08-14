class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        If the characters in a string s can be mapped to string t they are isomorphic
        Returns True if the map is successful, false otherwise
        '''
        if len(s) != len(t): #Not same length
            return False
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict: #Character not mapped yet
                if t[i] not in dict.values():
                    dict[s[i]] = t[i]
                else:
                    return False
            elif dict[s[i]] != t[i]: #Characters do not match map
                return False
        return True