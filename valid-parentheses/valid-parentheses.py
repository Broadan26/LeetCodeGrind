class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.insert(0, ch)
            elif ch == ')' and len(stack) > 0 and stack[0] == '(':
                stack.pop(0)
            elif ch == ']' and len(stack) > 0 and stack[0] == '[':
                stack.pop(0)
            elif ch == '}' and len(stack) > 0 and stack[0] == '{':
                stack.pop(0)
            else:
                return False
        return len(stack) == 0