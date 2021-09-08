class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        '''
        Given a string s and list of shifts, shifts the chars in string based on the shift list
        Returns the resulting shifted string as a string
        '''
        for i in range(len(shifts)-1, 0, -1): #Determine how much each letter shifts
            shifts[i-1] = shifts[i] + shifts[i-1]
        new_string = ''
        for i in range(len(s)):
            c = ord(s[i]) - 97 #Collect char info
            c = (c + shifts[i]) % 26 #Perform shift
            new_string += chr(c + 97) #Concatenate to new string
        return new_string