class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0 # Window start
        max_length = 0 # Max window size
        fruit_frequency = {}
        for end in range(len(fruits)):
            right_fruit = fruits[end]
            if right_fruit not in fruit_frequency: # Add to dict
                fruit_frequency[right_fruit] = 0
            fruit_frequency[right_fruit] += 1

            while len(fruit_frequency) > 2: # Need to start deleting fruits
                left_fruit = fruits[start]
                fruit_frequency[left_fruit] -= 1
                if fruit_frequency[left_fruit] == 0: # Check for window resize end
                    del fruit_frequency[left_fruit]
                start += 1
            max_length = max(max_length, end - start + 1) # Update max size

        return max_length