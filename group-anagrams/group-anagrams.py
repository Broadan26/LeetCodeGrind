class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Given an array of strings, this groups the anagrams together in lists
        Returns a list of all grouped together anagrams
        '''
        dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in dict:
                dict[key] = []
            dict[key].append(word)
        return dict.values()