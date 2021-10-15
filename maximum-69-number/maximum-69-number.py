class Solution:
    def maximum69Number (self, num: int) -> int:
        num_s = [str(ch) for ch in str(num)]
        for ch in range(len(num_s)):
            if num_s[ch] == '6':
                num_s[ch] = '9'
                break
        return int(''.join(num_s))