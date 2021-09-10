class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        '''
        Given a list of words and a pattern, checks if the words in the list follow the pattern
        Returns a list of the words that follow the pattern
        '''
        follows_pattern = []
        for word in words: #Check each word
            pattern_dict = {}
            flag = True
            for ch in range(len(word)): #Check the letters of each word
                if pattern[ch] not in pattern_dict: #Map based on pattern
                    if word[ch] not in pattern_dict.values(): #Check if mapping is a permutation
                        pattern_dict[pattern[ch]] = word[ch]
                    else:
                        flag = False
                        break
                else:
                    if pattern_dict[pattern[ch]] != word[ch]: #Check if mapping is a permutation
                        flag = False
                        break
            if flag: #Only append words following pattern
                follows_pattern.append(word)
        return follows_pattern