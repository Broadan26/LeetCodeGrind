class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        if len(s) < 1:
            return answer
        s_list = list(s)
        self.dfs(s_list, answer, 0)

        return answer
    
    def dfs(self, s_list: list[str], answer: list[str], count: int):
        if count >= len(s_list): # Base case, finished iterating
            answer.append(''.join(s_list))
            return

        while count < len(s_list) and not s_list[count].isalpha(): # Look for next char
            count += 1
        if count >= len(s_list): # End of string
            answer.append(''.join(s_list))
            return
        s_list[count]
        s_list[count] = s_list[count].lower()
        self.dfs(s_list, answer, count+1)
        s_list[count] = s_list[count].upper()
        self.dfs(s_list, answer, count+1)