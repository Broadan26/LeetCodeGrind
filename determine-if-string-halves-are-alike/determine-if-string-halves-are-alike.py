class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        start = 0
        end = len(s)-1
        cnt_start = cnt_end = 0
        while start < end:
            if s[start].lower() in vowels:
                cnt_start += 1
            if s[end].lower() in vowels:
                cnt_end += 1
            start += 1
            end -= 1
        return cnt_start == cnt_end