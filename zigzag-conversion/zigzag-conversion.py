class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Converts a string into a nonsensical zigzag pattern with a particular number of rows
        Returns the converted string as a string
        '''
        if numRows == 1: #No change to s
            return s
        convertedString = ''
        cycle = (2 * numRows) - 2
        for row in range(0, numRows): #Iterate through each row
            ch = 0
            while ch + row < len(s): #Iterate each character
                convertedString += s[ch + row] #Append to string
                if row != 0 and row != numRows - 1 and ch + cycle - row < len(s): #Leftovers
                    convertedString += s[ch + cycle - row]
                ch += cycle
        return convertedString