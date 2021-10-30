class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2,3,5] # Which factors we want to use
        num_factors = 3 # How many factors there are
        start = [0] * num_factors # Current value of each factor
        nums = [1] # List of divisible nums
        
        for i in range(n-1):
            
            # Create prime factor candidates and add lowest
            candidates = [factors[j] * nums[start[j]] for j in range(num_factors)] 
            new_num = min(candidates)
            
            # Add prime factor to list
            nums.append(new_num)
            
            # Update where prime factor starts
            start = [start[j] + (candidates[j] == new_num) for j in range(num_factors)]
        return nums[-1]