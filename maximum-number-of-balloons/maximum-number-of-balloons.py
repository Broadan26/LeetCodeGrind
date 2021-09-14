class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        '''
        Given a string, determines how many times 'balloon' can be spelled with the chars
        Returns the number of times 'balloon' can be spelled as an int
        '''
        from collections import Counter
        bal_dict = Counter(text)
        least = min((bal_dict['b']), bal_dict['a'])
        least = min((bal_dict['l'] // 2), least)
        least = min((bal_dict['o'] // 2), least)
        least = min(bal_dict['n'], least)
        return least