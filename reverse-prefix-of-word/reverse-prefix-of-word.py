class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        start = end = []
        for char in range(len(word)):
            if word[char] == ch:
                start = [word[it] for it in range(char, -1, -1)]
                end = [word[it] for it in range(char+1, len(word))]
                break
        return word if len(start) == 0 else ''.join(start + end)