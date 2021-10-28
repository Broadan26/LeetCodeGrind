class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower(): # All lower
            return True
        if word == word.upper(): # All upper
            return True
        if word == word.capitalize(): # First letter
            return True
        return False