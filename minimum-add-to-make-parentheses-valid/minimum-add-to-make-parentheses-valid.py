class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        p_stack = []
        invalids = 0
        for ch in s:
            if ch == '(': # Left opening, push to stack
                p_stack.append('(')
            elif ch == ')': # Right opening, check conditions
                if p_stack: # Stack has left opening, correct
                    p_stack.pop()
                else: # Stack is empty, invalid
                    invalids += 1
        return len(p_stack) + invalids