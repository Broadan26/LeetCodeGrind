class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        Given a string this function creates a new string based on character frequency
        Returns the new string with most frequent characters in front
        '''
        dict = {}
        for c in s: #Collect the number of items in the string
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        dict = sorted(dict.items(), key = lambda item:item[1], reverse = True) #Sort the dictionary based on key:value pair
        s = ''
        for key, number in dict: #Create the new string
            s += key * number
        return s