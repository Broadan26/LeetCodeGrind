class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        Given two strings s and t, finds the difference between them
        Returns the different character
        '''
        from collections import Counter
        dict_s = Counter(s) # Collect the char counts
        dict_t = Counter(t)
        dict_s.subtract(dict_t) # Take the difference of the dictionaries
        for key, value in dict_s.items(): # Find the difference
            if abs(value) == 1:
                return key