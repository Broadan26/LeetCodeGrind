class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        Given a string of chars in range A-Z in any combination, calculates the value
        Returns the sum as an int
        '''
        val_list = [(ord(c) -64) for c in columnTitle] #Get ascii val of chars and subtract 64
        loc = 1
        sum = 0
        for i in range(len(val_list)-1, -1, -1): #Calculates Base26 value of the number
            sum += val_list[i] * loc
            loc *= 26
        return sum