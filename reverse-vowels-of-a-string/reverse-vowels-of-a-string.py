class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        Given a string of characters, swaps the vowels of the string
        Returns the original string with swapped vowels
        '''

        def isVowel(ch: str) -> bool:
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': #Lowercase
                return True
            elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U': #Uppercase
                return True
            return False

        new_string = list(s)
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            while not isVowel(new_string[lo]) and lo < hi: #Iterate up
                lo += 1
            while not isVowel(new_string[hi]) and lo < hi: #Iterate down
                hi -= 1
            if lo <= hi: #Check if swap should occur
                new_string[lo], new_string[hi] = new_string[hi], new_string[lo]
                lo += 1
                hi -= 1
        return ''.join(new_string)