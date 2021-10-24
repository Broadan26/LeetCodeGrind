class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if word.rfind(pattern) != -1:
                count += 1
        return count