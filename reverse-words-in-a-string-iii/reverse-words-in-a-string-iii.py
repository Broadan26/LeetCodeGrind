class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ') # Make sentence mutable
        word_list = [[ch for ch in word]for word in word_list] # Make chars mutable
        word_list = [word[::-1] for word in word_list] # Reverse the words
        word_list = [''.join(word) for word in word_list] # Recombine words
        return ' '.join(word_list) # Return combined sentence