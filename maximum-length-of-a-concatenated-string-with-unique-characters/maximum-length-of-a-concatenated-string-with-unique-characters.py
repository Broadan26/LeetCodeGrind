class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Given an array of strings ,determines the longest concatenation of the stings with unique letters
        Returns the length of the longest string
        '''
        results = ['']
        max_size = 0
        for word in arr: #Utilize each word
            for i in range(len(results)): #Try each possible combination
                new_results = results[i] + word
                if len(new_results) == len(set(new_results)): #Unique characters only
                    results.append(new_results)
                    max_size = max(max_size, len(new_results)) #New max potential
        return max_size