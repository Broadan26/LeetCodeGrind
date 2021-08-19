class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        Converts an int value into base26
        Returns the base26 value
        '''
        answer = ''
        while columnNumber > 0:
            columnNumber -= 1 #Handles Z at 26
            value = 65 + (columnNumber % 26) #Base 26ify
            answer = chr(value) + answer #Answer will be in reverse order
            columnNumber //= 26
        return answer