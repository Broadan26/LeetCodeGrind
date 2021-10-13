class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest = float('-inf')
        smallest = float('inf')
        for num in nums: # Find smallest and largest O(n)
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
        print(largest, smallest)
        
        gcd = 1
        for num in range(2, smallest+1): # Check up to smallest O(n)
            if largest % num == 0 and smallest % num == 0:
                gcd = num
        return gcd