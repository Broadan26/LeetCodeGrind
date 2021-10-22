class Solution:
    # def checkPerfectNumber(self, num: int) -> bool:
    #     if num < 6: # Bad numbers
    #         return False
    #     num_sum = 0
    #     for i in range(1, num):
    #         if (num % i) == 0:
    #             num_sum += i
    #     return num_sum == num
    
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6: # Bad numbers
            return False
        num_sum = 0
        for i in range(2, int(sqrt(num))+1):
            if (num % i) == 0:
                num_sum += i
                num_sum += (num // i)
            if num_sum+1 > num:
                return False
        return num_sum+1 == num