class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        '''
        Given a string of length n, swaps the letters in reverse order
        Returns the modified string
        '''
        lo = 0
        hi = len(s) - 1
        mutable_string = list(s)
        while lo < hi:
            if self.checkIfLetter(mutable_string[lo]):
                while lo < hi:
                    if self.checkIfLetter(mutable_string[hi]):
                        mutable_string[lo], mutable_string[hi] = mutable_string[hi], mutable_string[lo]
                        hi -= 1
                        break
                    hi -= 1
            lo += 1
        return ''.join(mutable_string)

    def checkIfLetter(self, ch: str) -> bool:
        '''
        Helper function for revrseOnlyLetters
        Takes a character as a string and determines if it is an alphabetical character
        Returns True if so, False otherwise
        '''
        if ord(ch) > 64 and ord(ch) < 91: #Letter is uppercase
            return True
        if ord(ch) > 96 and ord(ch) < 123: #Letter is lowercase
            return True
        return False