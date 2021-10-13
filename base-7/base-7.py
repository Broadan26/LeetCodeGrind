class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
        num_list = []
        n = abs(num)
        while n > 0:
            remainder = n % 7
            num_list.append(str(remainder))
            n = n // 7
        return ''.join(num_list[::-1]) if num > 0 else '-'+''.join(num_list[::-1])