class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        cutoff = 0
        i = 0
        while i < length:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 1
                cutoff += 1
            i += 1
        while cutoff > 0:
            arr.pop(len(arr)-1)
            cutoff -= 1