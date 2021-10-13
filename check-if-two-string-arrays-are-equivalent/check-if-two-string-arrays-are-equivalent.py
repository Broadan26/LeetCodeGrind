class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_s = ''.join(word1) # Concatenate word1
        word2_s = ''.join(word2) # Concatenate word2
        return word1_s == word2_s # Check if same contents