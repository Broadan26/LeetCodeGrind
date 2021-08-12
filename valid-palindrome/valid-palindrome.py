class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Determines if the given string's alphanumeric chars are a palindrome
        Returns true if they are, false if not
        '''
        s_digits = []
        for i in s: #Cut out unnecessary characters
            if ord(i) > 64 and ord(i) < 91:
                s_digits.append(ord(i) + 32)
            elif ord(i) > 96 and ord(i) < 123:
                s_digits.append(ord(i))
            elif ord(i) > 47 and ord(i) < 58:
                s_digits.append(ord(i))
        left = 0
        right = len(s_digits) - 1
        while left <= right: #Iterate through cut down string
            if s_digits[left] == s_digits[right]:
                left += 1
                right -= 1
            else:
                return False
        return True