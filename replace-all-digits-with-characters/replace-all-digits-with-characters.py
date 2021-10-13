class Solution:
    def replaceDigits(self, s: str) -> str:
        s_list = list(s)
        for ch in range(0, len(s_list), 2):
            if ch+1 < len(s_list):
                s_list[ch+1] = chr(ord(s_list[ch]) + int(s_list[ch+1]))
        return ''.join(s_list)