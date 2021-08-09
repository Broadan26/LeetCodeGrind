class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Creates a list of all n well-formed parentheses combinations
        Returns a list of strings for all the combinations
        '''
        combos = []
        if n > 0: #If no parentheses pairs requested
            self.createStrings(combos,'', 0, 0, n)
        return combos
    def createStrings(self, combos: list[str], s: str, open: int, close: int, n: int):
        if len(s) == 2 * n and open == close:
            combos.append(s)
            return
        if open < n:
            s += '('
            self.createStrings(combos, s, open+1, close, n)
            s = s[:-1]
        if close < open:
            s += ')'
            self.createStrings(combos, s, open, close+1, n)
            s = s[:-1]