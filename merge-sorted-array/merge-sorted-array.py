class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        del nums1[m : len(nums1)]
        while i < (m + j) and j < n:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            else:
                i += 1
        while j < n:
            nums1.insert(i, nums2[j])
            j += 1
            i += 1