class Solution:
    def sumZero(self, n: int) -> list[int]:
        answer = []
        if n % 2 != 0: # Handle odd cases
            answer.append(0)
        
        # Append pos/neg num combos
        curr = 1
        for _ in range(len(answer), n, 2):
            answer.append(curr)
            answer.append(-answer[-1])
            curr += 1
        
        return answer