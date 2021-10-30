class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(sqrt(area)), 0, -1): # Run through sqrt of num
            instance = area / i
            if instance.is_integer(): # Check if division produces int
                return [int(instance), i]
        return [-1,-1]