class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for num in range(left, right+1): # Run thru nums inclusive
            for ch in str(num): # Break up num
                if int(ch) == 0 or num % int(ch) != 0: # Check if not divisible
                    break
            else: # Is divisible
                answer.append(num)
        return answer