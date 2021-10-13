class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_list = s.split(' ')
        return ' '.join(s_list[0:k])