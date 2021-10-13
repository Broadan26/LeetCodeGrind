class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s_list = [] # Make s mutable
        
        count = 0
        for ch in s:
            if ch == '(' and count > 0:
                s_list.append('(')
            elif ch == ')' and count > 1:
                s_list.append(')')
            count += 1 if ch == '(' else -1
        
        return ''.join(s_list) # Return reformed string