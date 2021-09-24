class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_dict = {}
        for i in range(len(arr)):
            if arr[i]*2 in num_dict:
                return True
            if arr[i] % 2 == 0 and arr[i] // 2 in num_dict:
                return True
            num_dict[arr[i]] = 1
        return False