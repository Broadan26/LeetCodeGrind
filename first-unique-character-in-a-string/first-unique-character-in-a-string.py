class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Returns the location of the first unique character in a string
        Returns the location as an int if found, -1 if not found
        '''
        dict = {}
        loc = -1
        for i, c in enumerate(s): #Store items in dictionary
            if c not in dict: #If item already seen, make it invalid
                dict[c] = i
            else:
                dict[c] = -1
        for i in dict: #Search for first unique
            if dict[i] != -1:
                loc = dict[i]
                break
        return loc