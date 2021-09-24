class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # Not mountainous
            return False

        left = 1
        while left < len(arr) and arr[left] > arr[left-1]: # Iterate the slope
            left += 1
        if left == 1 or left == len(arr): # Pointer did not move or reached end of list
            return False

        right = left # Swap to other side of the mountain peak
        while right < len(arr) and arr[right] < arr[right-1]: # Iterate the slope
            right += 1
        return right == len(arr) # Slope encompasses rest of the list