class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        Given a pattern to follow and a string, determines if the string follows the pattern
        Returns True if it does, false otherwise
        '''
        s_split = s.split(' ') #Pull out individual words to map
        if len(s_split) != len(pattern): #If length does not match, pattern fails
            return False
        dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in dict: #Determine if item in dictionary already
                if s_split[i] not in dict.values(): #Check reverse mapping
                    dict[pattern[i]] = s_split[i] #Add to dictionary
                else:
                    return False
            else:
                if dict[pattern[i]] != s_split[i]: #Not correct mapping
                    return False
        return True