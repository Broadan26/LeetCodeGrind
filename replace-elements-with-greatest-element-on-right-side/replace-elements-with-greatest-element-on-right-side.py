class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []

        right_max = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = right_max
            right_max = max(right_max, temp)
        return arr