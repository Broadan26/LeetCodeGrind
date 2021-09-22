class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # Sort the candidates list
        possible = [] # Possible list of values that can be the target
        answer = [] # The result to return

        def backtrack(possible: list[int], remainder: int, current: int, answer: list[list[int]]):
            if remainder == 0: # Current possibile combination equals target
                answer.append(list(possible))
                return
            
            for next_current in range(current, len(candidates)): #
                if next_current > current and candidates[next_current] == candidates[next_current-1]: # Avoid duplicate number usage
                    continue
                pick = candidates[next_current] # Found next usable number
                if (remainder - pick) < 0: # Not suitable for target
                    break

                possible.append(pick)
                backtrack(possible, remainder-pick, next_current+1, answer) # Recursively check picked value
                possible.pop() # End consideration of current number

        backtrack(possible, target, 0, answer)
        return answer