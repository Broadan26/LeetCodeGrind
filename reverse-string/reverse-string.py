class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''
        Given a list of characters, reverses the list
        Returns nothing, performs in-place mutable changes
        '''
        if len(s) < 2: #String is already reversed
            return
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1